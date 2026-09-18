# Status Report Instructions

## Overview
This guide explains how to complete each section of the status report template. A well-crafted status report provides stakeholders with clear visibility into project progress, risks, and team performance.

---

## Section-by-Section Instructions

### Report Header
**Purpose**: Identify the report and establish context.

**Instructions**:
- **Report Date**: Today's date in YYYY-MM-DD format
- **Reporting Period**: The week or sprint dates (e.g., Monday to Friday)
- **Project**: The official project or product name
- **Submitted By**: Your name and title/role

**Example**:
```
Report Date: 2026-09-16
Reporting Period: 2026-09-09 to 2026-09-16
Project: Contributor Analytics Dashboard
Submitted By: Jane Smith, Project Manager
```

---

### Executive Summary
**Purpose**: Provide a quick snapshot for busy stakeholders.

**Instructions**:
- Keep it brief: 2-3 sentences maximum
- Highlight the most important news (positive or concerning)
- Answer: What's the current state? What's the biggest concern or win?
- Use plain language; avoid jargon

**Tips**:
- Lead with status (on track, at risk, blocked)
- Mention any major milestone achieved this week
- Flag critical issues that need attention

**Example**:
```
The Contributor Analytics Dashboard is on track for delivery. 
We completed the Jira API integration and achieved 85% sprint velocity. 
One blocker on the authentication module was resolved Thursday.
```

---

### Current Status
**Purpose**: Provide a status snapshot in a scannable format.

**Instructions**:
- **Overall Status**: Choose ONE:
  - **GREEN**: Project is progressing as planned, no major concerns
  - **YELLOW**: Minor issues or delays, but manageable and on recovery plan
  - **RED**: Major blockers, significant delays, or escalation required

- **Sprint Status**: Is the sprint on track to meet its goals?
  - **ON TRACK**: Will complete committed story points
  - **AT RISK**: Likely to miss some commitments
  - **BLOCKED**: Cannot proceed without external intervention

- **Key Focus Areas**: List 2-3 primary initiatives this week

**Example**:
```
Overall Status: GREEN
Sprint Status: ON TRACK
Key Focus Areas:
  - Dashboard UI polish and responsiveness
  - Performance optimization for large datasets
  - Security audit and hardening
```

---

### Achievements This Week
**Purpose**: Celebrate progress and demonstrate momentum.

**Instructions**:
- List 3-5 concrete accomplishments
- Be specific: "Completed X" is better than "Made progress on X"
- Include both feature work and operational wins
- Mention milestones, releases, or bugs fixed

**Tips**:
- Use action verbs: completed, delivered, resolved, finalized
- Quantify where possible (e.g., "Fixed 12 critical bugs")
- Acknowledge team effort and collaboration

**Example**:
```
- Completed Jira API integration with full OAuth2 support
- Delivered responsive dashboard UI for mobile and desktop
- Resolved authentication blocker with IT security team
- Achieved 100% automated test coverage for core modules
- Onboarded 3 new team members and completed training
```

---

### Work In Progress
**Purpose**: Show ongoing efforts and expected timelines.

**Instructions**:
- List major work items (features, epics, or large tasks)
- **Owner**: Person or team responsible
- **% Complete**: Honest estimate of progress (0-100%)
- **Expected Completion**: Target date (YYYY-MM-DD format)

**Tips**:
- Focus on high-visibility items (not every small task)
- Update percentages weekly to track momentum
- Adjust dates early if delays are anticipated
- Row count: 3-7 items typically

**Example**:
```
| Item | Owner | % Complete | Expected Completion |
|------|-------|------------|-------------------|
| Defect analytics module | Alice Chen | 65% | 2026-09-23 |
| Performance optimization | Bob Martinez | 40% | 2026-09-30 |
| User documentation | Carol Lee | 85% | 2026-09-20 |
```

---

### Issues & Blockers
**Purpose**: Surface problems early and communicate solutions.

**Instructions**:
- List all significant issues preventing progress or quality
- **Severity**: 
  - HIGH: Blocks multiple people or delays critical path
  - MEDIUM: Impacts productivity but workarounds exist
  - LOW: Nice to resolve but doesn't block progress
- **Owner**: Who is taking action?
- **Impact**: How does this affect delivery or quality?
- **Resolution**: Proposed solution or timeline to fix

**Tips**:
- Be transparent; don't hide problems
- Every issue should have an owner and a proposed resolution
- Follow up on open issues each week
- Escalate HIGH severity items immediately

**Example**:
```
| Issue | Severity | Owner | Impact | Resolution |
|-------|----------|-------|--------|-----------|
| Jira API rate limiting | HIGH | David Park | Delays daily refresh task | Implement caching layer (by 2026-09-22) |
| Database timeout errors | MEDIUM | Emma Wilson | Intermittent dashboard errors | Scale DB instance (IT approval pending) |
```

---

### Metrics & Performance
**Purpose**: Quantify progress and team performance.

**Instructions**:
- **Sprint Velocity**: Story points completed ÷ story points committed
  - Example: "45 / 50 = 90%"
- **Completion Rate**: % of planned work items finished on time
- **Defect Rate**: Number of bugs discovered or fixed this week
- **Team Capacity**: Available team members ÷ total team size (accounts for absences)
- **On-Time Delivery**: % of items delivered by promised date

**Tips**:
- Track these metrics consistently each week
- Use trends to identify patterns (e.g., declining velocity → burnout)
- Celebrate high performance; investigate significant drops
- Metrics should tell a story about team health

**Example**:
```
Sprint Velocity: 42 / 50 (84%)
Completion Rate: 90%
Defect Rate: 8 bugs found, 6 fixed
Team Capacity Utilization: 90%
On-Time Delivery: 95%
```

---

### Risks & Mitigations
**Purpose**: Identify potential problems and plan ahead.

**Instructions**:
- List any foreseeable risks to delivery, quality, or team morale
- **Probability**: HIGH (likely to occur), MEDIUM, or LOW
- **Impact**: HIGH (major consequence), MEDIUM, or LOW
- **Mitigation Strategy**: Action plan to reduce risk or impact

**Tips**:
- Think 1-4 weeks ahead
- Include resource risks, technical risks, and schedule risks
- Every risk should have a mitigation plan
- Track risks each week and update status

**Example**:
```
| Risk | Probability | Impact | Mitigation Strategy |
|------|-------------|--------|-------------------|
| Key developer illness | MEDIUM | HIGH | Cross-train 2 backup devs on core modules |
| Jira API changes | LOW | HIGH | Monitor Jira release notes; test updates in staging |
| Scope creep | HIGH | MEDIUM | Weekly sprint planning review with PO |
```

---

### Next Week's Plan
**Purpose**: Set clear expectations for the upcoming week.

**Instructions**:
- List top 3-5 priorities for the coming week
- Be specific about what "done" looks like
- Align with sprint goals if applicable
- Include any meetings, reviews, or milestones

**Tips**:
- Priorities should flow logically from this week's progress
- Mention any external dependencies or approvals needed
- Communicate any planned absences or events

**Example**:
```
- Complete defect analytics module UI and integrate with backend
- Finish security audit and address critical findings
- Deploy to staging environment for QA testing
- Schedule demo with stakeholders (Thursday)
- Finalize user documentation and training materials
```

---

### Resource & Team Notes
**Purpose**: Communicate team capacity and morale.

**Instructions**:
- **Team Capacity**: How many people are available (e.g., "12 / 14")
- **Planned Absences**: Upcoming vacations, training, or events
- **Training/Development**: New skills, certifications, or blockers to learning
- **Other Notes**: Anything affecting team productivity

**Tips**:
- Transparency about capacity helps set realistic expectations
- Note upcoming absences early
- Mention team wins and morale boosters
- Share learning resources or opportunities

**Example**:
```
Team Capacity: 12 / 14 (2 on planned leave next week)
Planned Absences: Alice on vacation Sept 20-24; Bob on training Sept 17
Training/Development: 3 team members completed AWS certification
Other Notes: Team morale is high; great collaboration this sprint
```

---

### Stakeholder Updates
**Purpose**: Distill key messages for leadership and sponsors.

**Instructions**:
- Extract 2-3 important messages from the full report
- Focus on business impact: delivery, quality, risk, opportunity
- Use executive language (avoid technical jargon)
- Keep each message to 1-2 sentences

**Tips**:
- Lead with wins and progress
- Address any RED status or escalations immediately
- Tie progress to business goals (revenue, customer satisfaction, time to market)
- Be honest about delays or challenges

**Example**:
```
Key Messages for Leadership:
- Dashboard is on track for end-of-month delivery and will meet all business requirements
- Achieved 84% sprint velocity; team is performing well and morale is strong
- One security audit finding requires IT sign-off; working with IT to resolve by Sept 22
```

---

### Appendix
**Purpose**: Provide supporting details and reference materials.

**Instructions**:
- Attach or link to supporting documents (if needed)
- Examples: detailed sprint burndown, test result reports, architecture diagrams, links to live dashboards
- Keep this section minimal; refer to appendix only for stakeholders who need deep detail

**Tip**: Not all reports need an appendix. Use only if you have substantial supporting material.

---

## Best Practices

### Writing Tips
- **Be honest**: Acknowledge issues, delays, and concerns proactively
- **Be concise**: Busy stakeholders skim reports; use bullet points, tables, and short paragraphs
- **Be consistent**: Update the same metrics each week so trends are visible
- **Be actionable**: Every issue should have an owner and proposed next step

### Frequency & Distribution
- **Weekly reports** are typical for active projects
- **Distribute by Friday** so stakeholders have the week's summary for Monday planning
- **Send to**: Project sponsor, product owner, other key stakeholders

### Common Mistakes to Avoid
- ❌ Burying critical issues in text; always flag HIGH severity items
- ❌ Over-optimistic or over-pessimistic status ratings
- ❌ Unfinished action items with no owner or deadline
- ❌ Inconsistent metrics that make week-to-week trends unclear
- ❌ Too much detail; save specifics for appendix or follow-up conversations

---

## Questions & Examples
For a filled-in example report, see `example.md`.
