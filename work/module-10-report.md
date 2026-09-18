# Module 10 Completion Report

## Instruction Files
```text
    Directory: C:\SanjayNew\Github-Workspace-epam\hello-genai\work\module10-task\instructions


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----         9/17/2026   3:16 PM           2338 analyze-contributor-defect-metrics.agent.md
-a----         9/17/2026   3:16 PM           1671 apply-analytics-standards.agent.md
-a----         9/17/2026   3:16 PM           2154 calculate-sprint-summary.agent.md
-a----         9/17/2026  10:44 AM            984 create-status-report.agent.md
-a----         9/17/2026   2:53 PM           2004 creating-instructions.agent.md
-a----         9/17/2026   3:16 PM           2130 main.agent.md
```

## main.agent.md Contents
```markdown
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

- Important! Always follow this catalog first when a task involves an instruction workflow.
- Load the full catalog in each prompt so the latest instruction set is used.
- Keep instructions concise, actionable, and project-specific.
```

## Sample Instruction
- File: analyze-contributor-defect-metrics.agent.md
- Contents:
```markdown
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
```
