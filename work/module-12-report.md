# Module 12 Completion Report

## Instruction File
- Filename: use-metrics.agent.md

# Use Sprint Metrics Tool

- Use this instruction when a task requires sprint summary metrics from a list of issue records.
- Use `./tools/Metrics.py` to compute committed points, completed points, remaining points, completion percentage, created/resolved/active/blocked counts, and trend direction.
- Run the script with either a JSON file or a raw JSON array.
- Command examples:
  + `python ./tools/Metrics.py --issues-file ./sample_issues.json`
  + `python ./tools/Metrics.py --issues-json "[{\"status\":\"Done\",\"story_points\":8}]"`
- Input requirements:
  + The JSON payload must be a list of issue objects.
  + Each issue should include at least: `status` and `story_points`.
  + Missing or invalid story points are treated as 0.0 to keep the analysis stable.
  + Only issue records from the active sprint should be passed into the script.
- Processing behavior:
  + Filter to the active sprint before calculating metrics.
  + Sum story points for committed and completed work.
  + Compute remaining points as committed minus completed.
  + Compute completion percentage as completed / committed, capped safely between 0 and 100.
  + Count issues in created, resolved, active, and blocked states.
  + Report a trend direction of `ahead`, `behind`, or `neutral` based on the relative completion level.
- Output rules:
  + Print the results as JSON.
  + Keep the output concise and structured for dashboard or reporting use.
  + Use the returned values directly in UI or status reporting tasks.
- Constraints:
  + Do not infer unsupported values.
  + Do not pass non-array data to the script.
  + Do not include narrative text in the output if the goal is machine-readable metrics.
  + If no valid issues are supplied, return zeroed metrics rather than crashing.

## Script File
- Filename: Metrics.py
- Language: Python

import argparse
import json
import sys


def normalize_story_points(value):
    if value is None:
        return 0.0
    if isinstance(value, str):
        value = value.strip()
        if not value:
            return 0.0
        try:
            return float(value)
        except ValueError:
            return 0.0
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def compute_sprint_metrics(issues):
    if not issues:
        return {
            "committed_points": 0.0,
            "completed_points": 0.0,
            "remaining_points": 0.0,
            "completion_percentage": 0.0,
            "created_count": 0,
            "resolved_count": 0,
            "active_count": 0,
            "blocked_count": 0,
            "trend_direction": "neutral"
        }

    committed_points = 0.0
    completed_points = 0.0
    created_count = 0
    resolved_count = 0
    active_count = 0
    blocked_count = 0

    for issue in issues:
        status = str(issue.get("status", "")).strip().lower()
        story_points = normalize_story_points(issue.get("story_points"))

        committed_points += story_points

        if status in {"done", "resolved", "completed", "closed"}:
            completed_points += story_points
            resolved_count += 1
        elif status in {"in progress", "active", "todo", "to do", "new"}:
            active_count += 1
        elif "blocked" in status or "imped" in status:
            blocked_count += 1

        if issue.get("created") is not None:
            created_count += 1

    remaining_points = max(committed_points - completed_points, 0.0)
    completion_percentage = 0.0 if committed_points == 0 else (completed_points / committed_points) * 100

    if completion_percentage > 100:
        completion_percentage = 100.0
    if completion_percentage < 0:
        completion_percentage = 0.0

    if completed_points > committed_points:
        trend_direction = "ahead"
    elif completed_points < committed_points:
        trend_direction = "behind"
    else:
        trend_direction = "neutral"

    return {
        "committed_points": round(committed_points, 2),
        "completed_points": round(completed_points, 2),
        "remaining_points": round(remaining_points, 2),
        "completion_percentage": round(completion_percentage, 2),
        "created_count": created_count,
        "resolved_count": resolved_count,
        "active_count": active_count,
        "blocked_count": blocked_count,
        "trend_direction": trend_direction
    }


def parse_args():
    parser = argparse.ArgumentParser(description="Compute sprint summary metrics from issue data.")
    parser.add_argument("issues", nargs="?", help="JSON array string containing sprint issues.")
    parser.add_argument("--issues-file", dest="issues_file", help="Path to a JSON file containing the sprint issues.")
    parser.add_argument("--issues-json", dest="issues_json", help="JSON array string containing sprint issues.")
    return parser.parse_args()


def load_issues(value):
    if value is None:
        raise ValueError("Provide issue data as a JSON array, --issues-json, or --issues-file.")

    try:
        with open(value, "r", encoding="utf-8") as file:
            return json.load(file)
    except OSError:
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            raise ValueError("Issue data must be valid JSON or a path to a JSON file.")


def main():
    try:
        args = parse_args()
        issues_source = args.issues_file or args.issues_json or args.issues
        if issues_source is None:
            raise ValueError("Provide issue data as a JSON array, --issues-json, or --issues-file.")
        issues = load_issues(issues_source)
        if not isinstance(issues, list):
            raise ValueError("Issue data must be a JSON array of issue objects.")

        metrics = compute_sprint_metrics(issues)
        print(json.dumps(metrics, indent=2))
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

## Script Execution Output
---HELP:Metrics.py---
usage: Metrics.py [-h] [--issues-file ISSUES_FILE] [--issues-json ISSUES_JSON]
                  [issues]

Compute sprint summary metrics from issue data.

positional arguments:
  issues                JSON array string containing sprint issues.

options:
  -h, --help            show this help message and exit
  --issues-file ISSUES_FILE
                        Path to a JSON file containing the sprint issues.
  --issues-json ISSUES_JSON
                        JSON array string containing sprint issues.
---HELP:compound_interest.py---
Usage: python compound_interest.py <principal> <annual_rate> <compounds_per_year> <years>
