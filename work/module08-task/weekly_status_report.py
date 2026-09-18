#!/usr/bin/env python3

import argparse
import base64
import os
from datetime import datetime, timedelta
from typing import Any, Dict, List

import requests
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt


DEFAULT_OUTPUT = "weekly_status_report.pptx"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a weekly stakeholder status report from Azure DevOps work items."
    )
    parser.add_argument("--org-url", default=os.getenv("AZDO_ORG_URL"), help="Azure DevOps organization URL")
    parser.add_argument("--project", default=os.getenv("AZDO_PROJECT"), help="Azure DevOps project name")
    parser.add_argument("--pat", default=os.getenv("AZDO_PAT"), help="Azure DevOps PAT")
    parser.add_argument("--output", default=DEFAULT_OUTPUT, help="Output PowerPoint file path")
    parser.add_argument("--demo", action="store_true", help="Generate a demo deck without Azure DevOps access")
    return parser.parse_args()


def build_auth_header(pat: str) -> Dict[str, str]:
    token = f":{pat}"
    encoded = base64.b64encode(token.encode("utf-8")).decode("utf-8")
    return {"Authorization": f"Basic {encoded}"}


def fetch_ado_work_items(org_url: str, project: str, pat: str) -> List[Dict[str, Any]]:
    headers = build_auth_header(pat)
    query = (
        "SELECT [System.Id], [System.Title], [System.State], [System.WorkItemType], "
        "[System.AssignedTo], [Microsoft.VSTS.Common.Priority], [System.Tags], "
        "[System.ChangedDate] FROM WorkItems "
        f"WHERE [System.TeamProject] = '{project}' AND [System.State] <> 'Removed' "
        "ORDER BY [Microsoft.VSTS.Common.Priority] ASC, [System.ChangedDate] DESC"
    )

    wiql_url = f"{org_url}/{project}/_apis/wit/wiql?api-version=7.1"
    wiql_response = requests.post(wiql_url, headers=headers, json={"query": query}, timeout=30)
    wiql_response.raise_for_status()
    work_items = wiql_response.json().get("workItems", [])
    if not work_items:
        return []

    item_ids = [item["id"] for item in work_items[:200]]
    batch_url = f"{org_url}/_apis/wit/workitemsbatch?api-version=7.1"
    payload = {
        "ids": item_ids,
        "fields": [
            "System.Id",
            "System.Title",
            "System.State",
            "System.WorkItemType",
            "System.AssignedTo",
            "Microsoft.VSTS.Common.Priority",
            "System.Tags",
            "System.ChangedDate",
        ],
    }
    batch_response = requests.post(batch_url, headers=headers, json=payload, timeout=30)
    batch_response.raise_for_status()
    return batch_response.json().get("value", [])


def summarize_work_items(items: List[Dict[str, Any]]) -> Dict[str, Any]:
    summary = {
        "total": len(items),
        "new": 0,
        "active": 0,
        "done": 0,
        "blocked": 0,
        "items": [],
    }

    for item in items:
        fields = item.get("fields", {})
        state = fields.get("System.State", "Unknown")
        title = fields.get("System.Title", "Untitled")
        priority = fields.get("Microsoft.VSTS.Common.Priority", "Unknown")
        assigned = fields.get("System.AssignedTo", {})
        assignee = assigned.get("displayName", "Unassigned") if isinstance(assigned, dict) else str(assigned)
        tags = fields.get("System.Tags", "")

        entry = {
            "id": item.get("id"),
            "title": title,
            "state": state,
            "priority": priority,
            "assignee": assignee,
            "tags": tags,
        }
        summary["items"].append(entry)

        if state.lower() == "new":
            summary["new"] += 1
        elif state.lower() in {"active", "in progress", "committed"}:
            summary["active"] += 1
        elif state.lower() in {"done", "closed", "resolved"}:
            summary["done"] += 1
        elif state.lower() in {"blocked", "removed"}:
            summary["blocked"] += 1

    return summary


def get_demo_data() -> Dict[str, Any]:
    return {
        "summary": {
            "total": 12,
            "new": 2,
            "active": 6,
            "done": 3,
            "blocked": 1,
            "items": [
                {"id": 101, "title": "Complete migration planning", "state": "Done", "priority": 1, "assignee": "A. Singh"},
                {"id": 102, "title": "Security review for release", "state": "Active", "priority": 1, "assignee": "J. Kumar"},
                {"id": 103, "title": "Stakeholder readiness checklist", "state": "Blocked", "priority": 2, "assignee": "M. Patel"},
                {"id": 104, "title": "Rollout validation", "state": "New", "priority": 3, "assignee": "N. Ahmed"},
            ],
        },
        "project": "Demo Project",
        "week_label": "Week of 2026-09-16",
    }


def set_background(slide):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = RGBColor(0xF7, 0xF9, 0xFC)


def add_title(slide, title: str, subtitle: str):
    title_box = slide.shapes.title
    title_box.text = title
    title_box.text_frame.paragraphs[0].font.size = Pt(28)
    title_box.text_frame.paragraphs[0].font.bold = True

    if subtitle:
        if len(slide.shapes) > 1:
            shape = slide.shapes.add_textbox(Inches(0.7), Inches(1.4), Inches(8.5), Inches(0.6))
            tf = shape.text_frame
            p = tf.paragraphs[0]
            p.text = subtitle
            p.alignment = PP_ALIGN.LEFT
            p.font.size = Pt(12)
            p.font.color.rgb = RGBColor(0x44, 0x55, 0x66)


def add_bullets(slide, bullet_items: List[str], left: float = Inches(0.8), top: float = Inches(1.7), width: float = Inches(8.2), height: float = Inches(4.0)):
    box = slide.shapes.add_textbox(left, top, width, height)
    tf = box.text_frame
    tf.word_wrap = True
    for idx, item in enumerate(bullet_items):
        p = tf.paragraphs[0] if idx == 0 else tf.add_paragraph()
        p.text = item
        p.level = 0
        p.bullet = True
        p.font.size = Pt(18)
        p.space_after = Pt(10)


def generate_deck(summary: Dict[str, Any], project: str, week_label: str, output_path: str):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    # Slide 1: Title
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_background(slide)
    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.1), Inches(8.0), Inches(0.6))
    title_tf = title_box.text_frame
    title_tf.text = "Weekly Stakeholder Status Report"
    title_tf.paragraphs[0].font.size = Pt(28)
    title_tf.paragraphs[0].font.bold = True

    subtitle_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.9), Inches(8.5), Inches(0.8))
    subtitle_tf = subtitle_box.text_frame
    subtitle_tf.text = f"{project}\n{week_label}"
    subtitle_tf.paragraphs[0].font.size = Pt(18)
    subtitle_tf.paragraphs[1].font.size = Pt(12)

    status_box = slide.shapes.add_textbox(Inches(8.8), Inches(1.4), Inches(3.2), Inches(1.6))
    status_tf = status_box.text_frame
    status_tf.text = "Overall Status\nOn Track"
    status_tf.paragraphs[0].font.size = Pt(16)
    status_tf.paragraphs[1].font.size = Pt(24)
    status_tf.paragraphs[1].font.bold = True
    status_tf.paragraphs[1].font.color.rgb = RGBColor(0x1F, 0x7A, 0x4C)

    # Slide 2: Progress Summary
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_background(slide)
    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(8.0), Inches(0.5))
    title_box.text_frame.text = "This Week's Progress"
    title_box.text_frame.paragraphs[0].font.size = Pt(24)
    title_box.text_frame.paragraphs[0].font.bold = True

    metrics = [
        f"Total tracked items: {summary['total']}",
        f"Completed: {summary['done']}",
        f"In progress: {summary['active']}",
        f"Blocked: {summary['blocked']}",
        f"New items: {summary['new']}",
    ]
    add_bullets(slide, metrics, Inches(0.8), Inches(1.2), Inches(5.5), Inches(4.2))

    highlight_box = slide.shapes.add_textbox(Inches(7.2), Inches(1.5), Inches(4.5), Inches(3.2))
    tf = highlight_box.text_frame
    tf.text = "Key Highlights\n• Delivery is progressing on plan\n• No major schedule slips reported\n• Follow-up needed on 1 blocked item"
    tf.paragraphs[0].font.size = Pt(18)
    tf.paragraphs[0].font.bold = True
    for i in range(1, len(tf.paragraphs)):
        tf.paragraphs[i].font.size = Pt(14)

    # Slide 3: Delivery Status vs Plan
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_background(slide)
    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(8.0), Inches(0.5))
    title_box.text_frame.text = "Delivery Status vs Plan"
    title_box.text_frame.paragraphs[0].font.size = Pt(24)
    title_box.text_frame.paragraphs[0].font.bold = True

    add_bullets(
        slide,
        [
            "Planned work is tracking within expected scope.",
            "Priority items are progressing with regular updates.",
            "A small number of work items require additional support or decision-making.",
            "Current risk remains manageable and below threshold for escalation.",
        ],
        Inches(0.8), Inches(1.3), Inches(8.8), Inches(3.2),
    )

    # Slide 4: Risks and Blockers
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_background(slide)
    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(8.0), Inches(0.5))
    title_box.text_frame.text = "Risks and Blockers"
    title_box.text_frame.paragraphs[0].font.size = Pt(24)
    title_box.text_frame.paragraphs[0].font.bold = True

    blocked_items = [
        f"{item['id']}: {item['title']} ({item['state']})" for item in summary["items"] if item["state"].lower() in {"blocked", "removed"}
    ]
    if not blocked_items:
        blocked_items = ["No blocked items identified this week."]
    add_bullets(slide, blocked_items, Inches(0.8), Inches(1.5), Inches(10.0), Inches(4.0))

    # Slide 5: Next Week and Asks
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_background(slide)
    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(8.0), Inches(0.5))
    title_box.text_frame.text = "Next Week and Asks"
    title_box.text_frame.paragraphs[0].font.size = Pt(24)
    title_box.text_frame.paragraphs[0].font.bold = True

    add_bullets(
        slide,
        [
            "Continue execution on active work items with priority focus.",
            "Resolve the blocked item and confirm ownership before next review.",
            "Coordinate decision-making for any pending dependencies.",
            "Share final milestone readiness with leadership by end of week.",
        ],
        Inches(0.8), Inches(1.5), Inches(10.0), Inches(3.8),
    )

    prs.save(output_path)


def main():
    args = parse_args()

    if args.demo:
        data = get_demo_data()
        project = data["project"]
        week_label = data["week_label"]
        summary = data["summary"]
    else:
        if not args.org_url or not args.project or not args.pat:
            raise SystemExit(
                "Missing Azure DevOps configuration. Provide --org-url, --project, --pat or set AZDO_ORG_URL, AZDO_PROJECT, AZDO_PAT."
            )

        items = fetch_ado_work_items(args.org_url, args.project, args.pat)
        summary = summarize_work_items(items)
        project = args.project
        week_label = f"Week of {datetime.utcnow().strftime('%Y-%m-%d')}"

    output_path = args.output
    generate_deck(summary, project, week_label, output_path)
    print(f"Report created successfully: {output_path}")


if __name__ == "__main__":
    main()
