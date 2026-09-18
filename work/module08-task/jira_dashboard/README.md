# Jira Sprint Dashboard

This project creates a simple Jira Server sprint dashboard with:

- sprint completion progress bar
- story points completed vs remaining
- defect count
- blocked items
- current sprint vs previous sprint comparison

## Quick start

1. Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   python app.py
   ```
4. Open the browser at:
   ```text
   http://localhost:5000
   ```

## Configuration

Set the following environment variables if you want to connect to a real Jira Server instance:

```bash
set JIRA_URL=https://jira.example.com
set JIRA_USERNAME=your_username
set JIRA_PASSWORD=your_password
set JIRA_PROJECT_KEY=PROJ
```

If these are not set, the app uses sample sprint data so you can view the dashboard immediately.

## Dashboard focus

This is the first release optimized for the requirement we agreed on:

- audience: team leads and managers
- time range: current sprint vs previous sprint
- progress metric: story points + defects raised
- main visual: progress bar

## Files

- `app.py` — Flask app and Jira data loading logic
- `sample_data.json` — demo sprint data
- `templates/dashboard.html` — dashboard layout
- `static/style.css` — styling for the progress bar and cards
