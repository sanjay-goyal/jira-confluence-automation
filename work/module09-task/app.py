from __future__ import annotations

import json
import os
from datetime import date, timedelta
from pathlib import Path
from typing import Any, Dict, List

from flask import Flask, Response, render_template_string
from markdown import markdown


BASE_DIR = Path(__file__).resolve().parent
REPORTS_DIR = BASE_DIR / "reports"
DEFAULT_DATA_PATH = REPORTS_DIR / "sample_data.json"
DEFAULT_TEMPLATE_PATH = REPORTS_DIR / "template.md"


app = Flask(__name__)


def _default_report_data() -> Dict[str, Any]:
    report_date = date.today()
    start_date = report_date - timedelta(days=7)

    return {
        "report_date": report_date.isoformat(),
        "reporting_period": f"{start_date.isoformat()} to {report_date.isoformat()}",
        "project": "Contributor Analytics Dashboard",
        "submitted_by": "Jane Smith, Project Manager",
        "executive_summary": (
            "The Contributor Analytics Dashboard is on track for delivery. "
            "Core Jira integration, report formatting, and preview workflows are in place. "
            "The current focus is tightening the final presentation and making the report output easier to review."
        ),
        "current_status": {
            "overall_status": "GREEN",
            "sprint_status": "ON TRACK",
            "key_focus_areas": [
                "Finalize report formatting and preview behavior",
                "Stabilize data loading and fallback handling",
                "Validate output against the status report template",
            ],
        },
        "achievements_this_week": [
            "Implemented the status report template structure in markdown",
            "Added markdown-to-HTML preview support for the generated report",
            "Created a fallback data loader so the app works without external inputs",
        ],
        "work_in_progress": [
            {
                "item": "Data fetching module",
                "owner": "Engineering",
                "percent_complete": 80,
                "expected_completion": (report_date + timedelta(days=2)).isoformat(),
            },
            {
                "item": "Report formatting logic",
                "owner": "Engineering",
                "percent_complete": 75,
                "expected_completion": (report_date + timedelta(days=3)).isoformat(),
            },
            {
                "item": "Template alignment and preview polish",
                "owner": "Engineering",
                "percent_complete": 70,
                "expected_completion": (report_date + timedelta(days=4)).isoformat(),
            },
        ],
        "issues_blockers": [
            {
                "issue": "No sample data file was present in the workspace",
                "severity": "LOW",
                "owner": "Engineering",
                "impact": "The app needs a local fallback to stay runnable.",
                "resolution": "Use embedded demo data until a JSON feed is added.",
            }
        ],
        "metrics": {
            "sprint_velocity": "42 / 50",
            "completion_rate": "84%",
            "defect_rate": "2 bugs found, 1 fixed",
            "team_capacity_utilization": "90%",
            "on_time_delivery": "95%",
        },
        "risks_mitigations": [
            {
                "risk": "Report formatting drifts from the approved template",
                "probability": "MEDIUM",
                "impact": "MEDIUM",
                "mitigation_strategy": "Use the template file as the canonical reference and validate output against it.",
            },
            {
                "risk": "Future data source changes break local previews",
                "probability": "LOW",
                "impact": "MEDIUM",
                "mitigation_strategy": "Keep the embedded fallback data path and surface clear load errors in the UI.",
            },
        ],
        "next_weeks_plan": [
            "Wire the app to a real JSON source or API feed",
            "Add editing support for report sections",
            "Refine the generated markdown to match the template exactly",
        ],
        "resource_team_notes": {
            "team_capacity": "1 / 1",
            "planned_absences": "None",
            "training_development": "Working through Flask and markdown rendering patterns",
            "other_notes": "The module is intentionally self-contained so it can run without external services.",
        },
        "stakeholder_updates": [
            "The report generator is now runnable locally without external dependencies.",
            "The markdown preview reflects the approved section structure.",
            "Next step is connecting the app to a real report feed.",
        ],
        "appendix": [
            "Supporting data can be loaded from a JSON file when available.",
            "The preview supports both raw markdown and rendered HTML output.",
        ],
    }


def load_report_data() -> Dict[str, Any]:
    data_path = Path(os.getenv("REPORT_DATA_PATH", DEFAULT_DATA_PATH))
    if data_path.is_file():
        with data_path.open("r", encoding="utf-8") as file:
            return json.load(file)
    return _default_report_data()


def load_template_text() -> str:
  template_path = os.getenv("REPORT_TEMPLATE_PATH")
  if template_path:
    candidate = Path(template_path)
    if candidate.is_dir():
      candidate = candidate / "template.md"
    if candidate.is_file():
      return candidate.read_text(encoding="utf-8")

  template_dir = os.getenv("TEMPLATE_DIR")
  if template_dir:
    candidate = Path(template_dir) / "template.md"
    if candidate.is_file():
      return candidate.read_text(encoding="utf-8")

  if DEFAULT_TEMPLATE_PATH.is_file():
    return DEFAULT_TEMPLATE_PATH.read_text(encoding="utf-8")
    return "# Status Report Template\n"


def _format_bullets(items: List[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def _format_table(headers: List[str], rows: List[List[str]]) -> str:
    header_row = "| " + " | ".join(headers) + " |"
    separator_row = "|" + "|".join(["---"] * len(headers)) + "|"
    body_rows = ["| " + " | ".join(row) + " |" for row in rows]
    return "\n".join([header_row, separator_row, *body_rows])


def render_report_markdown(data: Dict[str, Any]) -> str:
    current_status = data["current_status"]
    resource_notes = data["resource_team_notes"]

    work_rows = [
        [
            item["item"],
            item["owner"],
            f"{item['percent_complete']}%",
            item["expected_completion"],
        ]
        for item in data["work_in_progress"]
    ]

    issue_rows = [
        [
            issue["issue"],
            issue["severity"],
            issue["owner"],
            issue["impact"],
            issue["resolution"],
        ]
        for issue in data["issues_blockers"]
    ]

    risk_rows = [
        [risk["risk"], risk["probability"], risk["impact"], risk["mitigation_strategy"]]
        for risk in data["risks_mitigations"]
    ]

    return f"""# Status Report

## Report Header
- **Report Date**: {data['report_date']}
- **Reporting Period**: {data['reporting_period']}
- **Project**: {data['project']}
- **Submitted By**: {data['submitted_by']}

---

## Executive Summary
{data['executive_summary']}

---

## Current Status
- **Overall Status**: {current_status['overall_status']}
- **Sprint Status**: {current_status['sprint_status']}
- **Key Focus Areas**:
{_format_bullets(current_status['key_focus_areas'])}

---

## Achievements This Week
{_format_bullets(data['achievements_this_week'])}

---

## Work In Progress
{_format_table(['Item', 'Owner', '% Complete', 'Expected Completion'], work_rows)}

---

## Issues & Blockers
{_format_table(['Issue', 'Severity', 'Owner', 'Impact', 'Resolution'], issue_rows)}

---

## Metrics & Performance
- **Sprint Velocity**: {data['metrics']['sprint_velocity']}
- **Completion Rate**: {data['metrics']['completion_rate']}
- **Defect Rate**: {data['metrics']['defect_rate']}
- **Team Capacity Utilization**: {data['metrics']['team_capacity_utilization']}
- **On-Time Delivery**: {data['metrics']['on_time_delivery']}

---

## Risks & Mitigations
{_format_table(['Risk', 'Probability', 'Impact', 'Mitigation Strategy'], risk_rows)}

---

## Next Week's Plan
{_format_bullets(data['next_weeks_plan'])}

---

## Resource & Team Notes
- **Team Capacity**: {resource_notes['team_capacity']}
- **Planned Absences**: {resource_notes['planned_absences']}
- **Training/Development**: {resource_notes['training_development']}
- **Other Notes**: {resource_notes['other_notes']}

---

## Stakeholder Updates
{_format_bullets(data['stakeholder_updates'])}

---

## Appendix
{_format_bullets(data['appendix'])}
"""


def render_report_html(data: Dict[str, Any]) -> str:
    report_markdown = render_report_markdown(data)
    rendered_markdown = markdown(report_markdown, extensions=["tables", "extra", "nl2br"])
    template_text = load_template_text()

    return render_template_string(
        """
        <!doctype html>
        <html lang="en">
        <head>
          <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <title>Status Report Preview</title>
          <style>
            :root {
              color-scheme: light;
              --bg: #f6f8fb;
              --panel: #ffffff;
              --text: #122033;
              --muted: #5a6b82;
              --accent: #0f766e;
              --border: #d9e2ec;
            }
            body {
              margin: 0;
              font-family: Arial, Helvetica, sans-serif;
              background: linear-gradient(180deg, #eef4f8 0%, var(--bg) 40%, #edf2f7 100%);
              color: var(--text);
            }
            .shell {
              max-width: 1100px;
              margin: 0 auto;
              padding: 32px 20px 48px;
            }
            .hero {
              background: var(--panel);
              border: 1px solid var(--border);
              border-radius: 18px;
              padding: 24px 28px;
              box-shadow: 0 18px 40px rgba(15, 23, 42, 0.08);
              margin-bottom: 20px;
            }
            .hero h1 {
              margin: 0 0 8px;
              font-size: 32px;
            }
            .hero p {
              margin: 4px 0;
              color: var(--muted);
            }
            .content, .template {
              background: var(--panel);
              border: 1px solid var(--border);
              border-radius: 18px;
              padding: 24px 28px;
              box-shadow: 0 18px 40px rgba(15, 23, 42, 0.05);
              margin-bottom: 20px;
              overflow-x: auto;
            }
            .content h2, .template h2 {
              margin-top: 1.5em;
            }
            table {
              width: 100%;
              border-collapse: collapse;
              margin: 16px 0;
            }
            th, td {
              border: 1px solid var(--border);
              padding: 10px 12px;
              text-align: left;
              vertical-align: top;
            }
            th {
              background: #f1f5f9;
            }
            pre {
              white-space: pre-wrap;
            }
            .meta {
              display: grid;
              grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
              gap: 12px;
              margin-top: 18px;
            }
            .meta div {
              background: #f8fafc;
              border: 1px solid var(--border);
              border-radius: 12px;
              padding: 12px;
            }
            .meta strong {
              display: block;
              margin-bottom: 4px;
              color: var(--accent);
            }
            .template h2 {
              margin-top: 0;
            }
            .template pre {
              background: #0f172a;
              color: #e2e8f0;
              border-radius: 14px;
              padding: 18px;
              overflow-x: auto;
            }
          </style>
        </head>
        <body>
          <main class="shell">
            <section class="hero">
              <h1>Status Report Preview</h1>
              <p>Rendered from local data with markdown formatting.</p>
              <div class="meta">
                <div><strong>Project</strong>{{ project }}</div>
                <div><strong>Report Date</strong>{{ report_date }}</div>
                <div><strong>Overall Status</strong>{{ overall_status }}</div>
                <div><strong>Sprint Status</strong>{{ sprint_status }}</div>
              </div>
            </section>

            <section class="content">
              {{ rendered_markdown|safe }}
            </section>

            <section class="template">
              <h2>Canonical Template</h2>
              <pre>{{ template_text }}</pre>
            </section>
          </main>
        </body>
        </html>
        """,
        rendered_markdown=rendered_markdown,
        template_text=template_text,
        project=data["project"],
        report_date=data["report_date"],
        overall_status=data["current_status"]["overall_status"],
        sprint_status=data["current_status"]["sprint_status"],
    )


@app.route("/")
def index() -> str:
    data = load_report_data()
    return render_report_html(data)


@app.route("/report.md")
def report_markdown() -> Response:
    data = load_report_data()
    return Response(render_report_markdown(data), mimetype="text/markdown")


@app.route("/api/report")
def report_json() -> Response:
    data = load_report_data()
    return Response(json.dumps(data, indent=2), mimetype="application/json")


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=True)