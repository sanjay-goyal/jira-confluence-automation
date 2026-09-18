# Contributor Analytics Dashboard - Implementation Backlog

This backlog translates the project specification into a concrete, actionable implementation plan for the MVP. It reflects the agreed priorities:
- Prioritize a working dashboard with sample data first.
- Keep scope limited to the MVP described in the spec.
- Sequence work in the order: Setup, Core Features, Integration, Testing, Documentation.

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
- [ ] Create a sample JSON dataset representing Jira issues, sprint metadata, assignees, defect records, and team activity.
- [ ] Define the normalized internal model for issue records, sprint state, contributor totals, defects, blockers, and trends.
- [ ] Build a transformation layer that maps raw Jira fields into a consistent app schema.
- [ ] Add a service abstraction so the UI can work against either sample data or live Jira data without code duplication.

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
- [ ] Detect the current active sprint from Jira or sample data and filter all metrics to that sprint only.
- [ ] Compute committed story points, completed points, remaining points, and sprint completion percentage.
- [ ] Calculate issue totals for created, resolved, active, and blocked items in the selected sprint.
- [ ] Add logic to handle missing or inconsistent story points without crashing the UI.
- [ ] Display raw values and trend direction together to avoid misleading interpretations.

### 2.3 Contributor analytics
- [ ] Aggregate issue counts by assignee for the active sprint.
- [ ] Aggregate story points delivered by contributor and compare each person against team totals.
- [ ] Count resolved issues by assignee and highlight the resolution rate for each contributor.
- [ ] Calculate workload distribution across the team of 14 contributors and identify overload/underload conditions.
- [ ] Build a sortable contributor table by contribution, workload, or unresolved issues.
- [ ] Add an indicator for contributors who are significantly above or below the team baseline.

### 2.4 Defect analytics
- [ ] Define which issue types or labels count as defects for the dashboard.
- [ ] Count defects raised, resolved, and open during the current sprint.
- [ ] Calculate defect-to-delivery ratio and defect trend by assignee or component when available.
- [ ] Surface severity or defect classification where Jira includes it.
- [ ] Present defect metrics separately from productivity metrics so quality is treated as a risk signal rather than simply lost output.

### 2.5 Blocker and risk detection
- [ ] Identify blocked issues using Jira status values, labels, custom fields, or explicit blocker indicators.
- [ ] Create a list of blocked items including assignee, issue key, summary, and blocker reason when available.
- [ ] Highlight risky items that are nearing due date or remain unresolved for an extended period.
- [ ] Count total blocked items and show them as a first-class operational risk metric.
- [ ] Ensure the blockers panel remains concise and readable in a single-page dashboard.

### 2.6 Activity timeline and trend view
- [ ] Aggregate issue creation and resolution activity by day or week within the sprint.
- [ ] Build a simple trend summary for intake and completion behavior over time.
- [ ] Compare activity patterns against expected sprint progress to surface risk or acceleration.
- [ ] Add labels or markers for spikes, dips, and unusual defect increase periods.
- [ ] Keep the trend view compact enough for a project manager to scan without extra drill-down.

## Phase 3: Integration

### 3.1 Jira connector
- [ ] Implement the Jira REST API client using the configured Jira Server/Data Center base URL and authentication settings.
- [ ] Add functions to fetch current sprint metadata, issue lists, and project-related fields from Jira.
- [ ] Support the Jira Server authentication model used by the environment, including basic or token-based access as required.
- [ ] Add timeout and retry handling for transient network or API errors.

### 3.2 Field extraction and normalization
- [ ] Map Jira issue fields into the app schema: issue key, summary, assignee, status, issue type, sprint, created date, updated date, resolution date, story points, labels, components, and defect metadata.
- [ ] Normalize missing or inconsistent fields such as empty assignees, absent story points, or missing component values.
- [ ] Standardize status values so blocked, risky, and completed work can be classified consistently.
- [ ] Add field fallback handling for custom story-point fields or alternative Jira configurations used by different projects.

### 3.3 Data processing pipeline
- [ ] Create the service layer that loads raw Jira data, transforms it, and computes dashboard metrics.
- [ ] Ensure only active sprint issues are used in sprint-level and contributor-level calculations.
- [ ] Compute summary metrics, workload balance, defect status, and blocker counts from cleaned data.
- [ ] Add a lightweight cache or snapshot mechanism to reduce unnecessary Jira calls during daily refresh cycles.
- [ ] Store the refresh timestamp and last success state for display in the dashboard header.

### 3.4 Daily refresh and resilience
- [ ] Implement a daily refresh routine that updates the dashboard data without restarting the application.
- [ ] Add a manual refresh action to support immediate data refresh during investigations.
- [ ] Gracefully handle Jira downtime, empty results, or partial failures with fallback messaging and safe defaults.
- [ ] Log failed API calls, transformation exceptions, and data-quality issues with enough context for debugging.
- [ ] Prevent refresh failures from breaking the current dashboard view or leaving users with an unusable UI.

## Phase 4: Testing

### 4.1 Unit tests for business logic
- [ ] Write tests for sprint summary calculations including committed, completed, and remaining story points.
- [ ] Write tests for contributor aggregation across multiple issue types and assignees.
- [ ] Write tests for defect totals, workload distribution, and issue resolution metrics.
- [ ] Write tests for blocker detection and risk flagging using status and date-based rules.
- [ ] Add tests for edge cases such as unassigned issues, missing story points, and incomplete Jira data.

### 4.2 API and integration tests
- [ ] Create mocked Jira responses for sprint lookup and issue retrieval.
- [ ] Verify the connector handles successful and failed API responses correctly.
- [ ] Validate the field normalization layer for custom fields, missing metadata, and inconsistent naming.
- [ ] Confirm the app can operate in sample-data mode and live-data mode without code changes.

### 4.3 UI smoke tests
- [ ] Add smoke tests for the dashboard home page and key sections.
- [ ] Verify KPI cards, sprint progress bar, contributor table, defect panel, and blockers view render correctly.
- [ ] Check for JavaScript or template-rendering issues in a modern browser environment.
- [ ] Validate the dashboard remains readable when values are zero, blank, or missing.

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
