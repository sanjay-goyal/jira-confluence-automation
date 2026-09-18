# Analyze Contributor and Defect Metrics

- Follow the rules in `./apply-analytics-standards.agent.md` before processing contributor and defect data.
- Input format:
  + Accept a filtered sprint dataset containing issue key, summary, assignee, status, issue type, sprint, story points, labels, components, created date, updated date, resolved date, and defect metadata when available.
  + Support both sample data and Jira-derived data.
  + Treat missing assignees, blank story points, and absent defect labels as empty values rather than fatal errors.
  + Use the active sprint only unless the caller explicitly requests a different scope.
- Processing steps:
  + Filter all calculations to the active sprint and remove unrelated issues before aggregating results.
  + For contributor analytics, group issues by assignee and compute issue counts, resolved counts, story points delivered, workload distribution, and unresolved item totals.
  + Compare each contributor against the team baseline to highlight overload, underload, and above/below-average performance.
  + For defect analytics, identify defect candidates using issue type, labels, custom fields, or project-specific defect rules.
  + Count defects raised, resolved, and open during the sprint, and calculate defect-to-delivery ratio and severity trends when data is present.
  + Summarize by assignee or component when available to expose risk concentration or uneven quality outcomes.
  + Flag risky contributors or defect clusters when the data indicates a meaningful imbalance, unresolved backlog, or elevated defect load.
- Output format:
  + Return concise Markdown with sections in this order: Contributor Analytics, Defect Analytics, Risk Signals.
  + Use bullet points only under each heading.
  + Show key metrics such as assignee totals, story points delivered, resolved issues, workload balance, defect counts, unresolved defects, and defect-to-delivery ratio.
  + Keep results brief, readable, and suitable for a project manager or team lead.
- Constraints:
  + If no contributors are available, write: "- No contributor data." under Contributor Analytics.
  + If no defect data is available, write: "- No defect data." under Defect Analytics.
  + If there are no significant risks, write: "- No major risk signals." under Risk Signals.
