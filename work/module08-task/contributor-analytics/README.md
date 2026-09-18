# Contributor Analytics Dashboard

This project provides a Jira Server-based contributor analytics dashboard for a project manager overseeing a team of 14 contributors on an enhancement project.

## Features

- Sprint completion progress bar
- Current sprint summary cards
- Contributor activity and workload analysis
- Defect counts and trend indicators
- Blocker and risk visibility
- Demo data mode for local testing
- Jira Server API integration mode for live data

## Stack

- Python
- Flask
- Jira REST API
- HTML/CSS

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure environment variables if using Jira Server:
   ```bash
   set JIRA_URL=https://jira.example.com
   set JIRA_USERNAME=your_user
   set JIRA_PASSWORD=your_password
   set JIRA_PROJECT_KEY=PROJ
   ```
4. Start the dashboard:
   ```bash
   python app.py
   ```
5. Open: http://127.0.0.1:5000

## Data source

- If the Jira environment variables are not set, the app loads demo data from `sample_data.json`
- If environment variables are set, the app attempts to fetch live Jira issue data for the active sprint

## Notes

This is the initial implementation based on the technical specification in `project_spec.md`.
