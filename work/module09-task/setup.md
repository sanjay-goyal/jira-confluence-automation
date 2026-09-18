# Development Setup Guide

This guide walks you through setting up the development environment for the Status Report module.

## Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- git

## Quick Start

### 1. Clone the Repository
```bash
cd /path/to/hello-genai/work
```

### 2. Create a Virtual Environment
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your configuration
# - FLASK_ENV: Set to 'development' or 'production'
# - SECRET_KEY: Generate a secure key for Flask sessions
# - REPORT_OUTPUT_DIR: Directory where reports will be saved
# - JIRA_* settings: Only needed if integrating with Jira
```

### 5. Verify Installation
```bash
python -c "import flask; print(f'Flask version: {flask.__version__}')"
```

You should see the Flask version printed without errors.

## Project Structure
```
module09-task/
├── .env.example          # Example environment configuration
├── requirements.txt      # Python dependencies
├── setup.md             # This file
├── reports/
│   ├── template.md      # Status report template
│   ├── instructions.md  # How to fill out reports
│   ├── example.md       # Filled-in example report
│   └── output/          # Directory for generated reports
└── app.py               # Main Flask application (to be created)
```

## Running the Application

Once the environment is set up:
```bash
# Activate virtual environment (if not already active)
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate      # Windows

# Run the Flask app
python app.py

# The app will be available at http://localhost:5000
```

## Common Issues

### Issue: `ModuleNotFoundError: No module named 'flask'`
**Solution**: Ensure you've activated your virtual environment and installed dependencies:
```bash
# Verify virtual environment is active (should see (venv) in prompt)
pip install -r requirements.txt
```

### Issue: `.env` file not being loaded
**Solution**: Ensure `.env` file exists in the project root and is NOT in `.gitignore`:
```bash
# Check if .env exists
ls -la .env  # macOS/Linux
dir .env     # Windows

# If missing, copy from template
cp .env.example .env
```

### Issue: Permission denied when creating virtual environment
**Solution**: Use the `--user` flag or ensure you have write permissions:
```bash
python -m venv --system-site-packages venv
```

## Deactivating the Virtual Environment

When you're done working, deactivate the virtual environment:
```bash
deactivate
```

## IDE Setup (Optional)

### VS Code
1. Install Python extension (ms-python.python)
2. Select interpreter: Ctrl+Shift+P → "Python: Select Interpreter"
3. Choose the virtual environment: `./venv/bin/python` (or `.venv\Scripts\python.exe` on Windows)

### PyCharm
1. Go to Settings → Project → Python Interpreter
2. Click gear icon → Add
3. Select "Existing Environment" and browse to `./venv/bin/python`

## Next Steps

After setup is complete:
- Review the status report template in `reports/template.md`
- Read the instructions in `reports/instructions.md`
- Check out the example report in `reports/example.md`
- Begin implementing features as outlined in Phase 2 of the project plan

## References

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)
- [Python-dotenv Documentation](https://python-dotenv.readthedocs.io/)
