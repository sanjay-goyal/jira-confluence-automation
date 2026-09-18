# Weekly Stakeholder Status Report Automation

This project generates a weekly executive status report for Azure DevOps work items and exports it as a PowerPoint deck.

## Features

- Connects to Azure DevOps via the REST API
- Pulls work item status, priority, and blocked items
- Builds a 5-slide stakeholder summary deck
- Supports a demo mode without Azure credentials

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
3. Set environment variables:
   ```bash
   set AZDO_ORG_URL=https://dev.azure.com/your-org
   set AZDO_PROJECT=your-project
   set AZDO_PAT=your-pat
   ```

## Run the generator

### Demo mode
```bash
python weekly_status_report.py --demo --output weekly-status-report.pptx
```

### Azure DevOps mode
```bash
python weekly_status_report.py --output weekly-status-report.pptx
```

## Output

The script creates a PowerPoint file in the project folder, with this structure:

1. Title slide
2. Weekly progress summary
3. Delivery status vs plan
4. Risks and blockers
5. Next week and asks

## Notes

- This is a starter template for a stakeholder-ready automation.
- You can customize colors, wording, and KPI logic to match your team style.
- Use a PAT with the appropriate Azure DevOps read permissions.
