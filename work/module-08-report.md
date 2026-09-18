# Module 08 Completion Report

## Tracked Files
.env.example
README.md
contributor-analytics/.env.example
contributor-analytics/README.md
contributor-analytics/app.py
contributor-analytics/project_spec.md
contributor-analytics/requirements.txt
contributor-analytics/sample_data.json
contributor-analytics/static/style.css
contributor-analytics/templates/dashboard.html
demo_weekly_status_report.pptx
jira_dashboard/.env.example
jira_dashboard/README.md
jira_dashboard/app.py
jira_dashboard/requirements.txt
jira_dashboard/sample_data.json
jira_dashboard/static/style.css
jira_dashboard/templates/dashboard.html
requirements.txt
weekly_status_report.py

## Spec Commit History
b0540d6 (HEAD -> master) module08 tasks

## project_spec.md Contents
# Contributor Analytics Dashboard - Technical Specification

## 1. Project Overview

This project will deliver a web-based contributor analytics dashboard for a project manager overseeing a team of 14 contributors on an enhancement project. The dashboard will pull activity data from Jira Server/Data Center and provide operational insight into team contribution, sprint health, workload balance, defects, and delivery trends.

The dashboard is intended to support day-to-day project management decisions rather than purely executive reporting. It will help the project manager answer questions such as:

- Who is contributing most actively?
- Which work items are blocked or delayed?
- Is the team delivering against sprint expectations?
- Who is overloaded or underutilized?
- Are defects increasing or trending down?
- What is the contribution pattern across the current sprint?

## 2. Interview Summary and Requirements Capture

The following requirements were validated during the interview:

- Primary user: project manager only
- Main objectives: track team activity, sprint health, workload balance, blocker visibility, and stakeholder-friendly project insights
- Data sources: Jira issues, stories, bugs, sprint data, assignee/team metadata, custom fields, labels, and component information
- Time window: current sprint only
- Output style: web dashboard
- Important metrics: issue creation/resolution trends, story points or effort delivered, defect count/severity, assignee workload distribution
- Team structure: one team of 14 contributors
- Refresh cycle: daily refresh
- Environment constraint: must support Jira Server/Data Center

## 3. Business Goals

### 3.1 Primary Goal
Provide a lightweight, data-driven operational dashboard to help the project manager understand team engagement and sprint health based on Jira activity.

### 3.2 Secondary Goals
- Detect workload imbalance across contributors
- Identify at-risk sprint items and blockers
- Monitor defect generation and resolution rates
- Support project tracking without requiring direct Jira query expertise
- Provide a single-page operational view for the project manager

## 4. Scope

### In Scope
- Jira Server integration
- Daily automated data refresh
- Current sprint analytics
- Team activity and contribution metrics
- Story points and issue trends
- Defect tracking
- Workload distribution
- Blocker and risk visibility
- Browser-based dashboard UI

### Out of Scope
- Real-time streaming updates
- Executive storytelling slides or presentation generation
- Jira write-back or workflow automation
- Multi-project cross-portfolio rollups
- Role-based access control for multiple user personas beyond project manager use

## 5. Users and Personas

### 5.1 Primary User
Project Manager

Responsibilities:
- Monitor sprint health and contributor output
- Identify issues, blockers, and trend changes
- Build confidence in team progress and delivery quality
- Support stakeholder updates with clear status evidence

### 5.2 Secondary User (Potential Future)
Team Leads

- Could access the same dashboard later with additional filters by sub-team or workstream

## 6. Functional Requirements

### 6.1 Data Ingestion
The application shall:
- connect to Jira Server/Data Center via REST API
- authenticate using configured credentials
- fetch issue data for the active sprint
- include story, bug, task, and related metadata
- extract assignee, status, issue type, custom fields, labels, sprint keys, and timestamps

### 6.2 Data Processing
The application shall:
- calculate current sprint totals
- aggregate issue activity by contributor
- compute story points completed and remaining
- count issue creation/resolution activity
- count defects raised and resolved
- identify blocked items and at-risk work
- calculate per-person workload distribution

### 6.3 Dashboard Views
The dashboard shall include the following modules:

1. Sprint Summary
   - sprint name and status
   - total committed story points
   - completed story points
   - remaining story points
   - sprint completion percentage

2. Contribution Analytics
   - issue count by contributor
   - story points by contributor
   - resolved issues by contributor
   - activity trend by contributor

3. Defect Analytics
   - defects raised in current sprint
   - defects resolved
   - open defects
   - defect trend by assignee or component

4. Workload Balance
   - contribution distribution across 14 contributors
   - utilization comparison between contributors
   - overload and underload indicators

5. Blocker and Risk View
   - blocked items count
   - list of blocked items with assignee and reason
   - risky items nearing due date or in unresolved state

6. Team Activity Timeline
   - daily or weekly issue creation/resolution activity
   - historical pattern within current sprint

### 6.4 User Experience Requirements
- Dashboard must be a single-page web application
- Layout must be readable and scannable in under 10 seconds
- Priority metrics must be visible without drilling down
- Use cards, labels, and progress bars for quick interpretation
- Dashboard should render in modern browsers

## 7. Non-Functional Requirements

### 7.1 Performance
- Initial dashboard load should complete in under 5 seconds for standard sprint data
- Daily refresh should not degrade Jira API responsiveness significantly

### 7.2 Reliability
- Application should gracefully handle Jira API failures or unavailable data
- Use fallbacks for missing fields or network issues
- Logs should capture failed API requests and processing exceptions

### 7.3 Maintainability
- Code should be modular
- Jira API logic and dashboard logic should be separated
- Configuration should be stored in environment variables

### 7.4 Security
- Jira credentials must not be hard-coded in source files
- Secrets must be stored in environment variables or secure configuration
- The app should be deployed behind internal access controls if used beyond local testing

## 8. Technical Architecture

### 8.1 Recommended Stack
- Backend: Python + Flask
- Data access: Jira REST API client using requests
- Frontend: HTML + CSS + lightweight JavaScript
- Data processing: Python business logic for metrics aggregation
- Persistence: optional JSON cache or local snapshot for daily refresh

### 8.2 High-Level Components
1. Jira Connector
   - fetches sprint data and issue metadata
2. Data Transformer
   - normalizes fields and aggregates metrics
3. Analytics Engine
   - computes contributor metrics and trends
4. Dashboard Layer
   - renders KPI cards, progress bars, activity summaries, and tables
5. Scheduler
   - refreshes data once per day

## 9. Data Model Requirements

### 9.1 Required Jira Fields
The dashboard should consume, at minimum:
- issue key
- summary
- assignee
- status
- issue type
- sprint
- created date
- updated date
- resolution date
- story points or equivalent effort field
- labels
- components
- defect classification/severity if present

### 9.2 Derived Metrics
The app shall compute:
- issue count per assignee
- story points completed per assignee
- issue resolution rate
- defect-to-delivery ratio
- blocked item count
- completion percentage
- contribution distribution percentage

## 10. Dashboard Design Requirements

### 10.1 Layout
The dashboard will contain the following sections:
- header with sprint name and refresh timestamp
- primary KPI cards
- sprint progress bar
- contributor contribution table
- defect summary panel
- blockers list
- trend panel

### 10.2 Visual Elements
- KPI cards with color coding
- Green for healthy metrics
- Yellow for caution conditions
- Red for blocked or at-risk conditions
- Progress bars for sprint completion
- Bar or table views for contributor comparison

### 10.3 Interaction Needs
- Filter by assignee or status if feasible
- Sort contributors by contribution or workload
- Highlight over- and under-loaded contributors
- Allow quick drill into issue lists for active blockers if implemented later

## 11. Rules for Team Contribution Analysis

To avoid misleading interpretation, the dashboard should:
- count only active sprint issues in the selected sprint window
- distinguish between issue count and story points to prevent misread of task size
- treat defects as a quality signal, not purely a productivity penalty
- display raw values and trend direction together
- flag likely workload imbalance when one contributor has significantly higher load than others

## 12. Security and Compliance Considerations

- Jira authentication should use secure configuration and not commit credentials to source control
- The project manager dashboard should be restricted to internal network or authorized users only
- Data exposure should be limited to project-relevant Jira fields and issue metadata

## 13. Risks and Dependencies

### Risks
- Jira custom fields may have inconsistent naming or missing values
- Story points may not be consistently populated for all issue types
- Defect taxonomy may vary across teams or projects
- Jira Server APIs may require specific permissions or additional configuration

### Dependencies
- Valid Jira Server endpoint access
- Jira credentials with read access to project issues and sprint data
- Consistent project and sprint naming conventions
- Approval for which issue types count as defects

## 14. Acceptance Criteria

The project will be considered successful when:

1. A web dashboard loads successfully using sample data when no Jira credentials are configured
2. The dashboard loads real Jira Server sprint data when environment variables are configured
3. Sprint summary metrics are visible without manual filtering
4. Team contribution metrics are grouped by contributor
5. Defect count and blocker count are displayed clearly
6. The dashboard reflects current sprint metrics and is easily refreshed daily
7. The dashboard is readable on a standard desktop browser

## 15. Implementation Plan

### Phase 1: Baseline Dashboard
- Connect to Jira Server using REST API
- Pull current sprint issues
- Calculate summary metrics
- Render KPI cards and sprint progress bar

### Phase 2: Contributor Analytics
- Build assignee-level breakdown
- Add contribution tables and workload balance indicators
- Add defect analysis and blockers view

### Phase 3: Enhancement and Refinement
- Add sorting and filters
- Improve styling and readability
- Add daily refresh automation and logs

## 16. Recommended MVP Scope

The first release should prioritize:
- current sprint only
- single team of 14 contributors
- story points + defect metrics
- sprint completion bar
- contributor contribution summary
- blocker view

This MVP is small enough to implement in a focused iteration while still delivering clear value to the project manager.

## 17. Summary

This contributor analytics dashboard is designed to give the project manager a clear operational view of team activity from Jira Server. The initial scope focuses on the most valuable metrics: sprint progress, contributor activity, defect trends, and blockers. The dashboard is intentionally centered on the project manager use case and will be built as a simple, maintainable web application with daily refresh capability.
