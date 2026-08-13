# PS-Delivery Quality Metrics Tracker

A web application for tracking delivery quality KPIs across Professional Services (PS) project types. Built for CXC delivery leaders to monitor, measure, and improve project execution quality from pre-engagement through post-implementation.

## Features

- **5 Project Types** — Matured PDI, Emerging PDI, Brown Field Transformation, Migration, and Upgrade, each with stage-specific KPIs sourced from PSTG Quality Metrics standards.
- **Per-Project Tracking** — Create a tracker per project with customer details, team roster, technology, and scope. KPIs auto-populate based on the selected project type.
- **Stage-by-Stage Metrics** — Track KPIs across every delivery stage (Pre Engagement, Design, Implementation, Testing, Post Implementation, Overall Project) with support for percentage, count, score, and yes/no inputs.
- **Dashboard** — Visual overview with Chart.js charts showing project distribution by type, status breakdown, and average stage completion across active projects.
- **KPI Summary Reference** — Interactive summary slides (sourced from PSTG Quality KPI Summary PPTX) with tabbed views per project type, plus detailed accordion tables with full KPI definitions, formulas, and measurement guidance.
- **Search & Filter** — Find projects by name, customer, PM, or technology; filter by project type or status from the sidebar.
- **Auto-Start Service** — Configured as a macOS Launch Agent so the app starts on login and auto-restarts if it goes down.

## Tech Stack

| Component   | Technology                    |
|-------------|-------------------------------|
| Backend     | Python / Flask                |
| Database    | SQLite (via Flask-SQLAlchemy) |
| Frontend    | HTML, CSS, JavaScript         |
| Charts      | Chart.js                      |
| Styling     | Custom CSS (Cisco brand)      |

## Project Structure

```
├── app.py                  # Flask routes and application logic
├── models.py               # SQLAlchemy models (Project, Engineer, MetricEntry)
├── metrics_config.py       # KPI definitions per project type + summary slide data
├── requirements.txt        # Python dependencies
├── start.sh                # Launch script for the macOS service
├── .gitignore
├── METRICS_UPDATE_GUIDE.md # How to manually update KPI definitions
├── static/
│   ├── css/style.css       # All application styles
│   └── js/
│       ├── app.js          # Sidebar navigation logic
│       └── dashboard.js    # Chart.js dashboard visualizations
└── templates/
    ├── base.html           # Base layout with sidebar and top bar
    ├── dashboard.html      # Dashboard with summary cards and charts
    ├── projects.html       # Project listing with filters
    ├── project_form.html   # Create / edit project form
    ├── project_detail.html # Project detail with stage tabs and metric inputs
    └── reference.html      # KPI summary slides + detailed definitions
```

## Setup

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/mgjc19/CXC-Quality-KPI-Tracking-App.git
cd CXC-Quality-KPI-Tracking-App

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

The app will be available at **http://127.0.0.1:5050**.

### Auto-Start on macOS (Launch Agent)

A Launch Agent plist is included for persistence. To install:

```bash
cp com.mgjc.delivery-tracker.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.mgjc.delivery-tracker.plist
```

This will auto-start the app on login and restart it if it crashes. Logs go to `/tmp/delivery-tracker.log`.

**Useful commands:**

```bash
# Stop the service
launchctl unload ~/Library/LaunchAgents/com.mgjc.delivery-tracker.plist

# Start the service
launchctl load ~/Library/LaunchAgents/com.mgjc.delivery-tracker.plist

# Check logs
cat /tmp/delivery-tracker.log
```

## Updating KPIs

KPI definitions live in `metrics_config.py`. See [METRICS_UPDATE_GUIDE.md](METRICS_UPDATE_GUIDE.md) for detailed instructions on how to add, modify, or remove KPIs, stages, and project types.

## License

Internal use — Cisco Confidential.
