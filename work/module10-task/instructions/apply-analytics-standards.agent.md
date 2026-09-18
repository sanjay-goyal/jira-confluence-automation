# Apply Shared Analytics Standards

- Use these rules as the common foundation for sprint, contributor, and defect analytics work.
- Input format:
  + Accept issue data from either sample data or live Jira-derived sources.
  + Require issue records to include at least: issue key, summary, status, sprint, assignee, story points, created date, updated date, and issue type.
  + Keep the analysis scoped to the active sprint unless the caller explicitly requests a different time range.
  + Treat missing values as empty or 0 only when that default is safe and clearly documented.
- Processing steps:
  + Filter data to the active sprint before performing any aggregation.
  + Normalize values consistently so status, story points, assignees, and defect indicators are comparable.
  + Handle incomplete or inconsistent records without crashing the workflow or injecting unsupported assumptions.
  + Prefer accurate calculations grounded in the dataset over speculative or inferred values.
- Output format:
  + Return concise Markdown with brief bullet-point sections.
  + Keep the result readable for project managers and team leads.
  + Keep the output compact and focused on the metrics that matter most.
- Constraints:
  + Do not use tables, long paragraphs, or narrative explanation.
  + Do not include filler words, marketing language, or speculative conclusions.
  + Keep the final status-report output under 20 lines when used in a status update.
  + If a value is unavailable, state the missing-data condition clearly instead of inventing a result.
- Reference this file from task-specific instructions that need the common analytics rules.
