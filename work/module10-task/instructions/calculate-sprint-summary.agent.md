# Calculate Sprint Summary Metrics

- Follow the rules in `./apply-analytics-standards.agent.md` before processing sprint data.
- Input format:
  + Accept a list of issue records or Jira-like objects containing at least: issue key, summary, status, sprint, assignee, story points, created date, updated date, resolution date, and issue type.
  + Support both sample data and live Jira data.
  + Treat missing or blank story points as 0 for safe calculation unless a different default is explicitly required by the project.
  + If sprint metadata is absent, infer the active sprint from the latest sprint in the dataset.
- Processing steps:
  + Select the active sprint and filter all metrics to issues belonging to that sprint only.
  + Normalize issue status values into consistent categories such as completed, active, blocked, and unresolved.
  + Sum committed story points from all issues in the selected sprint.
  + Sum completed story points from resolved or done issues.
  + Calculate remaining story points as committed minus completed.
  + Compute sprint completion percentage as completed points divided by committed points, with a floor of 0 and a cap of 100 when values are not available or invalid.
  + Count created, resolved, active, and blocked issues in the selected sprint.
  + Preserve raw values and trend direction together when presenting the result.
- Output format:
  + Return Markdown with these headings in order: Accomplishments, Blockers, Next Week.
  + Use only bullet points under each heading.
  + Include sprint summary values in a concise, business-friendly format.
  + Show metrics such as committed points, completed points, remaining points, sprint completion percentage, created issues, resolved issues, active issues, and blocked issues.
  + Keep the output concise and readable for a project manager or team lead.
- Constraints:
  + If no blocker exists, write: "- No blockers." under Blockers.
  + If no future work is planned, write: "- No planned items." under Next Week.
  + If committed points are zero or missing, report completion as 0% and state the issue clearly in the summary.
