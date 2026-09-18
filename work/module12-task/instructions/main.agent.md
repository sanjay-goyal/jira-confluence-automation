# Instructions Catalog

Each entry below is an instruction file with a brief description of when to use it.

- [`./create-status-report.agent.md`](./create-status-report.agent.md) — create concise weekly project status updates in Markdown.
  + Keywords: status report, weekly report, progress update, blockers, next week
  + Target: `**/*.md`
  + Exceptions: use only for project update reports

- [`./creating-instructions.agent.md`](./creating-instructions.agent.md) — create or refine reusable instruction files for project workflows.
  + Keywords: create instruction, add instruction, update instructions, workflow guide
  + Target: `**/*.md`
  + Exceptions: use when a process should be captured as a reusable instruction

- [`./calculate-sprint-summary.agent.md`](./calculate-sprint-summary.agent.md) — compute sprint summary metrics from active sprint issue data.
  + Keywords: sprint summary, sprint metrics, committed points, completed points, sprint completion
  + Target: `**/*.md`, `**/*.py`, `**/*.json`
  + Exceptions: use when aggregating issue data for a single sprint

- [`./analyze-contributor-defect-metrics.agent.md`](./analyze-contributor-defect-metrics.agent.md) — aggregate contributor performance and defect metrics for the active sprint.
  + Keywords: contributor analytics, defect analytics, workload, defect ratio, assignee metrics
  + Target: `**/*.md`, `**/*.py`, `**/*.json`
  + Exceptions: use when reviewing team delivery and software quality signals

- [`./apply-analytics-standards.agent.md`](./apply-analytics-standards.agent.md) — shared rules for sprint, contributor, and defect analytics across project metrics work.
  + Keywords: analytics standards, shared rules, metrics validation, safe defaults
  + Target: `**/*.md`, `**/*.py`, `**/*.json`
  + Exceptions: use as the common rule set for analytics instructions

- [`./calculate-compound-interest.agent.md`](./calculate-compound-interest.agent.md) — calculate compound interest for a principal amount, annual rate, compounding frequency, and duration.
  + Keywords: compound interest, investment growth, future value, interest calculator
  + Target: `**/*.py`, `**/*.md`
  + Exceptions: use only for interest calculations and not for sprint analytics

- [`./use-metrics.agent.md`](./use-metrics.agent.md) — instruct how to run the sprint summary metrics script with issue data.
  + Keywords: sprint metrics, use metrics, summary metrics, dashboard metrics, issue data
  + Target: `**/*.py`, `**/*.json`, `**/*.md`
  + Exceptions: use when computing or reporting sprint summary metrics

- Important! Always follow this catalog first when a task involves an instruction workflow.
- Load the full catalog in each prompt so the latest instruction set is used.
- Keep instructions concise, actionable, and project-specific.
