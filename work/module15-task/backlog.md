# Contributor Analytics Dashboard - Implementation Backlog

This backlog translates the project specification into a concrete, actionable implementation plan for the MVP. It reflects the agreed priorities:
- Prioritize a working dashboard with sample data first.
- Keep scope limited to the MVP described in the spec.
- Sequence work in the order: Setup, Core Features, Integration, Testing, Documentation.

Approach legend:
- Approach 1 = single-file or single-item comparison/check
- Approach 2 = iterative review across a small set of files or items
- Approach 3 = batch or script-driven processing across many files/data records

## Phase 1: Setup

### 1.1 Project initialization
- [ ] Create the Flask application structure with separate folders for app logic, templates, static assets, sample data, and configuration.
- [ ] Add the Python project dependency list for Flask, requests, python-dotenv, and any supporting libraries required for rendering and data processing.
- [ ] Confirm the app can start locally and render a basic page without Jira access.
- [ ] Establish a simple project layout consistent with the dashboard architecture: connector, transformer, analytics, UI, and config modules.

### 1.2 Configuration and environment setup
- [ ] Define environment variables for Jira base URL, authentication credentials, project key, sprint selection, and refresh configuration.
- [ ] Add configuration loading from environment variables and validate required values before the app begins processing data.
- [ ] Implement safe fallback behavior so the dashboard still loads with sample data when credentials are missing.
- [ ] Document the local setup steps required to run the app on a developer workstation.

### 1.3 Sample data and data model
- [ ] Create a sample JSON dataset representing Jira issues, sprint metadata, assignees, defect records, and team activity. (Approach 3)
- [ ] Define the normalized internal model for issue records, sprint state, contributor totals, defects, blockers, and trends. (Approach 2)
- [ ] Build a transformation layer that maps raw Jira fields into a consistent app schema. (Approach 3)
- [ ] Add a service abstraction so the UI can work against either sample data or live Jira data without code duplication. (Approach 2)

## Phase 2: Core Features

### 2.1 Dashboard shell
- [ ] Build the single-page dashboard layout with a header showing sprint name, refresh timestamp, and status summary.
- [ ] Add primary KPI cards for sprint completion, committed points, completed points, remaining points, and active defects.
- [ ] Add a sprint progress bar and completion percentage indicator for the current sprint.
- [ ] Create a contributor section with a table that lists issue counts, points delivered, and resolved work by assignee.
- [ ] Add a defect summary panel and blocker/risk summary section to the main dashboard.
- [ ] Add a basic activity/trend panel for issue creation and resolution patterns across the sprint.
- [ ] Apply the required color rules for healthy, caution, and blocked states.

### 2.2 Sprint summary metrics
- [ ] Detect the current active sprint from Jira or sample data and filter all metrics to that sprint only. (Approach 3)
- [ ] Compute committed story points, completed points, remaining points, and sprint completion percentage. (Approach 3)
- [ ] Calculate issue totals for created, resolved, active, and blocked items in the selected sprint. (Approach 3)
- [ ] Add logic to handle missing or inconsistent story points without crashing the UI. (Approach 2)
- [ ] Display raw values and trend direction together to avoid misleading interpretations. (Approach 2)

### 2.3 Contributor analytics
- [ ] Aggregate issue counts by assignee for the active sprint. (Approach 3)
- [ ] Aggregate story points delivered by contributor and compare each person against team totals. (Approach 3)
- [ ] Count resolved issues by assignee and highlight the resolution rate for each contributor. (Approach 3)
- [ ] Calculate workload distribution across the team of 14 contributors and identify overload/underload conditions. (Approach 3)
- [ ] Build a sortable contributor table by contribution, workload, or unresolved issues. (Approach 2)
- [ ] Add an indicator for contributors who are significantly above or below the team baseline. (Approach 2)

### 2.4 Defect analytics
- [ ] Define which issue types or labels count as defects for the dashboard.
- [ ] Count defects raised, resolved, and open during the current sprint.
- [ ] Calculate defect-to-delivery ratio and defect trend by assignee or component when available.
- [ ] Surface severity or defect classification where Jira includes it.
- [ ] Present defect metrics separately from productivity metrics so quality is treated as a risk signal rather than simply lost output.

### 2.5 Blocker and risk detection
- [ ] Identify blocked issues using Jira status values, labels, custom fields, or explicit blocker indicators. (Approach 3)
- [ ] Create a list of blocked items including assignee, issue key, summary, and blocker reason when available. (Approach 3)
- [ ] Highlight risky items that are nearing due date or remain unresolved for an extended period. (Approach 3)
- [ ] Count total blocked items and show them as a first-class operational risk metric. (Approach 2)
- [ ] Ensure the blockers panel remains concise and readable in a single-page dashboard. (Approach 1)

### 2.6 Activity timeline and trend view
- [ ] Aggregate issue creation and resolution activity by day or week within the sprint. (Approach 3)
- [ ] Build a simple trend summary for intake and completion behavior over time. (Approach 3)
- [ ] Compare activity patterns against expected sprint progress to surface risk or acceleration. (Approach 2)
- [ ] Add labels or markers for spikes, dips, and unusual defect increase periods. (Approach 2)
- [ ] Keep the trend view compact enough for a project manager to scan without extra drill-down. (Approach 1)

## Phase 3: Integration

### 3.1 Jira connector
- [ ] Implement the Jira REST API client using the configured Jira Server/Data Center base URL and authentication settings. (Approach 3)
- [ ] Add functions to fetch current sprint metadata, issue lists, and project-related fields from Jira. (Approach 3)
- [ ] Support the Jira Server authentication model used by the environment, including basic or token-based access as required. (Approach 2)
- [ ] Add timeout and retry handling for transient network or API errors. (Approach 2)

### 3.2 Field extraction and normalization
- [ ] Map Jira issue fields into the app schema: issue key, summary, assignee, status, issue type, sprint, created date, updated date, resolution date, story points, labels, components, and defect metadata. (Approach 3)
- [ ] Normalize missing or inconsistent fields such as empty assignees, absent story points, or missing component values. (Approach 3)
- [ ] Standardize status values so blocked, risky, and completed work can be classified consistently. (Approach 2)
- [ ] Add field fallback handling for custom story-point fields or alternative Jira configurations used by different projects. (Approach 2)

### 3.3 Data processing pipeline
- [ ] Create the service layer that loads raw Jira data, transforms it, and computes dashboard metrics. (Approach 3)
- [ ] Ensure only active sprint issues are used in sprint-level and contributor-level calculations. (Approach 3)
- [ ] Compute summary metrics, workload balance, defect status, and blocker counts from cleaned data. (Approach 3)
- [ ] Add a lightweight cache or snapshot mechanism to reduce unnecessary Jira calls during daily refresh cycles. (Approach 2)
- [ ] Store the refresh timestamp and last success state for display in the dashboard header. (Approach 1)

### 3.4 Daily refresh and resilience
- [ ] Implement a daily refresh routine that updates the dashboard data without restarting the application.
- [ ] Add a manual refresh action to support immediate data refresh during investigations.
- [ ] Gracefully handle Jira downtime, empty results, or partial failures with fallback messaging and safe defaults.
- [ ] Log failed API calls, transformation exceptions, and data-quality issues with enough context for debugging.
- [ ] Prevent refresh failures from breaking the current dashboard view or leaving users with an unusable UI.

## Phase 4: Testing

### 4.1 Unit tests for business logic
- [ ] Write tests for sprint summary calculations including committed, completed, and remaining story points. (Approach 3)
- [ ] Write tests for contributor aggregation across multiple issue types and assignees. (Approach 3)
- [ ] Write tests for defect totals, workload distribution, and issue resolution metrics. (Approach 3)
- [ ] Write tests for blocker detection and risk flagging using status and date-based rules. (Approach 3)
- [ ] Add tests for edge cases such as unassigned issues, missing story points, and incomplete Jira data. (Approach 3)

### 4.2 API and integration tests
- [ ] Create mocked Jira responses for sprint lookup and issue retrieval. (Approach 3)
- [ ] Verify the connector handles successful and failed API responses correctly. (Approach 3)
- [ ] Validate the field normalization layer for custom fields, missing metadata, and inconsistent naming. (Approach 3)
- [ ] Confirm the app can operate in sample-data mode and live-data mode without code changes. (Approach 2)

### 4.3 UI smoke tests
- [ ] Add smoke tests for the dashboard home page and key sections. (Approach 3)
- [ ] Verify KPI cards, sprint progress bar, contributor table, defect panel, and blockers view render correctly. (Approach 3)
- [ ] Check for JavaScript or template-rendering issues in a modern browser environment. (Approach 2)
- [ ] Validate the dashboard remains readable when values are zero, blank, or missing. (Approach 2)

### 4.4 Failure-path testing
- [ ] Test missing credentials and graceful fallback behavior if live Jira data is unavailable.
- [ ] Test Jira timeout and 403/500-style failures.
- [ ] Test malformed JSON or partially populated issue objects.
- [ ] Verify the app logs the failing stage and root cause clearly for support and maintenance.

## Phase 5: Documentation

### 5.1 User documentation
- [ ] Write a project README that explains the dashboard purpose, target users, and key outcomes.
- [ ] Document local setup steps for installing dependencies and running the dashboard.
- [ ] Document required environment variables and example values for Jira Server access.
- [ ] Add short troubleshooting guidance for missing data, failed Jira calls, and sample-data mode.

### 5.2 Technical documentation
- [ ] Describe the architecture: Jira connector, data transformer, analytics engine, and dashboard layer.
- [ ] Document the normalized data model and the Jira fields required for the app.
- [ ] Explain the refresh process and how cached data is used for daily updates.
- [ ] Record assumptions and known limitations such as inconsistent Jira field naming or missing story points.

### 5.3 Operational documentation
- [ ] Document deployment considerations for internal-only access and secure credential handling.
- [ ] Describe how to validate the app in sample mode before enabling live Jira integration.
- [ ] Note the expected logging and support behavior for operational maintenance.
- [ ] Add a concise MVP checklist for handoff and future enhancement work.

## Recommended MVP Delivery Sequence

- [ ] Phase 1: Setup and baseline sample-data dashboard
- [ ] Phase 2: Core sprint summary and contributor analytics
- [ ] Phase 3: Jira integration and refresh flow
- [ ] Phase 4: Testing and reliability validation
- [ ] Phase 5: Documentation and handoff

## Definition of Done for the MVP

- [ ] The dashboard loads successfully with sample data when Jira credentials are unavailable.
- [ ] The dashboard loads real Jira sprint data when environment variables are set.
- [ ] Sprint summary metrics are visible without manual filtering.
- [ ] Team contribution metrics are grouped by contributor.
- [ ] Defect, blocker, and workload indicators are displayed clearly.
- [ ] The dashboard refreshes daily and handles failures gracefully.
- [ ] The app is documented clearly enough for local setup and operational use.
