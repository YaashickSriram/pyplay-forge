@"
# Sycamore Interview Prep

7-day automation engineering sprint. Python + Playwright + Pytest framework targeting QA Sr. Test Engineer (Automation) role at Sycamore Informatics.

## Status: Day 1 — Python foundations & utilities

## Setup
``````powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
``````

## Structure
- ``/exercises`` — Python practice
- ``/utils`` — reusable helpers (logger, file I/O, config)
- ``/framework`` — core framework (Day 4+)
- ``/pages`` — Page Objects (Day 3+)
- ``/api_clients`` — API clients (Day 2+)
- ``/tests`` — test suites
"@ | Out-File -FilePath README.md -Encoding utf8