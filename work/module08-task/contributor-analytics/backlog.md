# Contributor Analytics Dashboard - Implementation Backlog

This backlog is derived from the project specification and reflects the agreed priorities:
- Prioritize real Jira Server integration early in the work.
- Keep scope aligned to the MVP described in the spec.
- Sequence work in the order: Setup, Core Features, Integration, Testing, Documentation.

## Phase 1: Setup

### 1.1 Project foundation
- [ ] Create the Flask application skeleton with a clear project structure for routes, services, templates, static assets, and configuration.
- [ ] Create the Python dependency manifest with Flask, requests, python-dotenv, and any supporting packages needed for charting or formatting.
- [ ] Establish a standard folder layout for app code, templates, static CSS, sample data, and environment configuration.
- [ ] Confirm the project works locally with a minimal app boot sequence and a basic landing page.

### 1.2 Configuration and environment
- [ ] Define required environment variables for Jira base URL, username, password/token, project key, and sprint selection.
- [ ] Add configuration loading from environment variables and validate missing values with clear startup errors.
- [ ] Add a safe fallback mode so the dashboard works with sample data when credentials are absent.
- [ ] Document local development setup steps for Windows and standard Python environments.

### 1.3 Baseline data handling
- [ ] Create a lightweight sample JSON dataset matching the expected Jira issue shape for testing without live Jira access.
- [ ] Define the internal data model for issues, sprint metadata, assignees, defects, blockers, and activity records.
- [ ] Establish a consistent field-mapping layer so Jira data can be normalized before metric calculation.
- [ ] Add a stub service pattern so the app can swap between sample data and Jira data without changing the UI logic.

## Phase 2: Core Features

### 2.1 Dashboard shell and layout
- [ ] Build the single-page dashboard layout with a header showing sprint name, refresh time, and status indicators.
- [ ] Add KPI card sections for sprint health, completed points, remaining work, and active defects.
- [ ] Add a sprint progress bar and supporting text for completion percentage and remaining effort.
- [ ] Create a contributor summary section with sortable rows for contribution totals and workload balance.
- [ ] Add a blocker and risk panel listing blocked items with assignee and reason.
- [ ] Add a defects panel and a trend or activity panel for sprint-level insights.
- [ ] Apply the required visual conventions: green for healthy, yellow for caution, red for blocked or at-risk states.

### 2.2 Sprint summary metrics
- [ ] Implement logic to detect the current active sprint and select only issues in that sprint window.
- [ ] Calculate committed story points, completed story points, remaining story points, and sprint completion percentage.
- [ ] Compute total issue count, resolved issue count, and active issue count for the sprint summary.
- [ ] Add formatting for raw values plus trend direction to avoid misread interpretation.
- [ ] Handle missing story points or unestimated work safely using fallback values and clear labels.

### 2.3 Contributor analytics
- [ ] Aggregate issue counts by assignee for active sprint issues.
- [ ] Aggregate story points delivered by assignee and compare against team totals.
- [ ] Count resolved issues by assignee and show issue resolution rate per contributor.
- [ ] Identify active contributions by daily or weekly trend within the current sprint.
- [ ] Calculate workload distribution across the 14 contributors and flag imbalance using relative thresholds.
- [ ] Build a contributor table sorted by contribution, workload, or unresolved items.
- [ ] Add visual indicators for overloaded and underutilized contributors.

### 2.4 Defect and quality metrics
- [ ] Define which Jira issue types or labels count as defects for the dashboard.
- [ ] Count defects raised, defects resolved, and currently open defects in the sprint.
- [ ] Compute defect-to-delivery ratio and defect trend by assignee or component.
- [ ] Surface severity and issue classification when available from Jira fields.
- [ ] Separate quality signal from productivity signal so defects are treated as operational risk rather than simple output loss.

### 2.5 Blockers and risk tracking
- [ ] Identify blocked issues using Jira status, resolution, and custom fields or labels.
- [ ] Create a list of blocked items showing assignee, issue key, summary, and blocker reason when available.
- [ ] Highlight risky work nearing due date or remaining unresolved for too long.
- [ ] Add logic to flag items that require project manager attention.
- [ ] Present blocked and risky items in a concise panel without overwhelming the main dashboard.

### 2.6 Activity timeline and trend view
- [ ] Aggregate issue creation and resolution activity by day or week within the current sprint.
- [ ] Create a trend chart or summary for intake and completion patterns over time.
- [ ] Compare current sprint activity to the implied expected pace or completion curve.
- [ ] Add labels and annotations for notable spikes, dips, or defect increases.
- [ ] Ensure the view remains readable in a single-page dashboard without excessive detail.

## Phase 3: Integration

### 3.1 Jira connector
- [ ] Implement a Jira REST API client using the configured base URL and authentication credentials.
- [ ] Add functions to fetch active sprint metadata, issue lists, and project-level data using Jira Server/Data Center APIs.
- [ ] Support authentication patterns compatible with Jira Server, including token or basic auth as configured by the environment.
- [ ] Add retry logic and timeout handling for transient API errors.

### 3.2 Field extraction and normalization
- [ ] Map Jira issue fields to the internal schema: issue key, summary, assignee, status, issue type, created date, updated date, response fields, sprint data, labels, components, and story points.
- [ ] Normalize missing values such as empty assignee, missing story points, or absent custom fields.
- [ ] Standardize status values for risk classification, blocker detection, and sprint tracking.
- [ ] Identify and configure alternative field names for story points or equivalent effort fields used by Jira projects.

### 3.3 Data processing pipeline
- [ ] Build the service layer responsible for loading raw Jira data, transforming it, and aggregating all dashboard metrics.
- [ ] Ensure only active sprint issues are included in contributor and sprint calculations.
- [ ] Compute summary, contributor, defect, and blocker metrics from normalized data sets.
- [ ] Add a lightweight caching strategy or JSON snapshot for daily refresh without excessive API calls.
- [ ] Store refresh timestamp and last successful data pull for display in the dashboard header.

### 3.4 Daily refresh and resilience
- [ ] Implement a scheduled refresh routine that updates dashboard data once per day.
- [ ] Add a manual refresh trigger from the dashboard or admin entry point for immediate updates.
- [ ] Handle Jira outages and partial data failures gracefully with fallback messages and safe defaults.
- [ ] Log failed API requests, data normalization issues, and processing exceptions with meaningful context.
- [ ] Make sure slow or failing refreshes do not break the existing displayed dashboard state.

## Phase 4: Testing

### 4.1 Unit tests for calculations
- [ ] Write tests for sprint summary calculations, including points committed, completed, and remaining.
- [ ] Write tests for contributor aggregation across multiple issue types and assignees.
- [ ] Write tests for defect counting and workload distribution logic.
- [ ] Write tests for blocker and risk detection based on status and due-date conditions.
- [ ] Add tests for edge cases such as unassigned issues, missing story points, and incomplete Jira payloads.

### 4.2 API and integration tests
- [ ] Create mocked Jira API responses for active sprint fetches and issue list retrieval.
- [ ] Verify the connector handles valid success responses and malformed error responses correctly.
- [ ] Test the mapping layer for field normalization, custom field fallback, and missing metadata.
- [ ] Validate that the app can operate in sample-data mode and in live Jira mode without code changes.

### 4.3 UI and smoke tests
- [ ] Add smoke tests for the dashboard homepage rendering and key sections.
- [ ] Verify KPI cards, sprint progress, tables, defect panels, and blocker lists are visible.
- [ ] Check the page loads without JavaScript errors in a modern browser environment.
- [ ] Validate the dashboard remains readable and scannable when data values are zero or missing.

### 4.4 Reliability and failure-path testing
- [ ] Test missing credentials and graceful fallback behavior when live Jira data is unavailable.
- [ ] Test network timeouts or 500/403 responses from Jira.
- [ ] Test malformed JSON, missing fields, and partially populated issue records.
- [ ] Verify logs clearly capture the failing stage and root cause for supportability.

## Phase 5: Documentation

### 5.1 User-facing documentation
- [ ] Write a project README explaining the purpose, dashboard features, and target users.
- [ ] Document setup steps for installing dependencies and running the app locally.
- [ ] Document required environment variables and example values for Jira Server configuration.
- [ ] Add a short troubleshooting guide for missing data, unavailable Jira access, and fallback mode.

### 5.2 Technical documentation
- [ ] Document the app architecture, including Jira connector, transformer, analytics engine, and dashboard layer.
- [ ] Describe the internal data model and the Jira fields used for the dashboard.
- [ ] Explain the refresh and cache flow for daily sprint updates.
- [ ] Capture assumptions and known limitations such as custom field differences or story point inconsistencies.

### 5.3 Operational documentation
- [ ] Document deployment considerations for internal access controls and secure configuration.
- [ ] Describe how to validate the app with sample data before enabling full Jira integration.
- [ ] Document support and logging expectations for production use.
- [ ] Add release notes or a brief MVP checklist for handoff or future enhancement work.

## Recommended MVP Delivery Sequence

- [ ] Phase 1: Setup and baseline sample-data dashboard
- [ ] Phase 2: Core sprint summary and contributor analytics
- [ ] Phase 3: Jira integration and daily refresh
- [ ] Phase 4: Testing and reliability validation
- [ ] Phase 5: Documentation and handoff

## Definition of Done for the MVP

- [ ] The dashboard loads successfully with sample data when Jira credentials are unavailable.
- [ ] The dashboard loads live Jira sprint data when environment variables are configured.
- [ ] Sprint summary metrics are visible without manual filtering.
- [ ] Contributor and defect breakdowns are grouped and displayed clearly.
- [ ] Blockers and workload imbalance are surfaced in a readable format.
- [ ] The dashboard can be refreshed daily and handles errors gracefully.
- [ ] Documentation is sufficient for local setup and day-to-day operation.
