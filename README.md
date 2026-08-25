# PS-Delivery Quality Metrics Tracker

A web application for tracking delivery quality KPIs across Professional Services (PS) project types. Built for CXC delivery leaders to monitor, measure, and improve project execution quality from pre-engagement through post-implementation.

---

## Features

- **5 Project Types** — Matured PDI, Emerging PDI, Brown Field Transformation, Migration, and Upgrade, each with stage-specific KPIs sourced from PSTG Quality Metrics standards.
- **Per-Project Tracking** — Create a tracker per project with customer details, team roster, technology, and scope. KPIs auto-populate based on the selected project type.
- **Stage-by-Stage Metrics** — Track KPIs across every delivery stage (Pre Engagement, Design, Implementation, Testing, Post Implementation, Overall Project) with support for percentage, count, score, and yes/no inputs.
- **Dashboard** — Visual overview with Chart.js charts showing project distribution by type, status breakdown, and average stage completion across active projects.
- **KPI Summary Reference** — Interactive summary slides (sourced from PSTG Quality KPI Summary PPTX) with tabbed views per project type, plus detailed accordion tables with full KPI definitions, formulas, and measurement guidance.
- **Search & Filter** — Find projects by name, customer, PM, or technology; filter by project type or status from the sidebar.
- **Auto-Start Service** — Configured as a macOS Launch Agent so the app starts on login and auto-restarts if it goes down.

---

## Tech Stack

| Component   | Technology                    |
|-------------|-------------------------------|
| Backend     | Python 3.10+ / Flask 3.1      |
| Database    | SQLite (via Flask-SQLAlchemy)  |
| ORM         | Flask-SQLAlchemy 3.1           |
| Frontend    | HTML5, CSS3, JavaScript (ES6) |
| Charts      | Chart.js 4.x                  |
| Styling     | Custom CSS (Cisco brand)       |
| Persistence | macOS Launch Agent (launchd)   |

---

## Project Structure

```
CXC-Quality-KPI-Tracking-App/
├── app.py                  # Flask routes, API endpoints, application logic
├── models.py               # SQLAlchemy models (Project, Engineer, MetricEntry)
├── metrics_config.py       # KPI definitions per project type + summary slide data
├── requirements.txt        # Python dependencies
├── start.sh                # Launch script (used by macOS Launch Agent)
├── .gitignore
├── README.md
├── METRICS_UPDATE_GUIDE.md # How to manually update KPI definitions
├── static/
│   ├── css/
│   │   └── style.css       # All application styles (Cisco-branded)
│   └── js/
│       ├── app.js          # Sidebar navigation logic
│       └── dashboard.js    # Chart.js dashboard visualizations
└── templates/
    ├── base.html           # Base layout with sidebar, top bar, Cisco logo
    ├── dashboard.html      # Dashboard with summary cards and charts
    ├── projects.html       # Project listing with search and filters
    ├── project_form.html   # Create / edit project form
    ├── project_detail.html # Project detail with stage tabs and metric inputs
    └── reference.html      # KPI summary slides + detailed definition tables
```

---

## Setup

### Prerequisites

- Python 3.10 or later
- pip
- macOS (for auto-start; the app itself runs on any OS)

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
python3 app.py
```

The app will be available at **http://127.0.0.1:5050**.

### Quick Start (without activating venv)

```bash
./start.sh
```

This calls the venv's Python directly, so no manual activation is needed.

---

## Auto-Start on macOS (Launch Agent)

A macOS Launch Agent keeps the app running permanently — it auto-starts on login and restarts if it ever crashes or gets killed.

### How it works

The Launch Agent plist (`com.mgjc.delivery-tracker.plist`) is installed at:

```
~/Library/LaunchAgents/com.mgjc.delivery-tracker.plist
```

It runs the venv's Python binary directly against `app.py`, with `KeepAlive` set to `true`.

### Managing the service

```bash
# Stop the app
launchctl unload ~/Library/LaunchAgents/com.mgjc.delivery-tracker.plist

# Start the app
launchctl load ~/Library/LaunchAgents/com.mgjc.delivery-tracker.plist

# Check status
launchctl list | grep delivery

# View logs
cat /tmp/delivery-tracker.log

# Tail logs in real time
tail -f /tmp/delivery-tracker.log
```

### Reinstalling after a path change

If you move or rename the project folder, update the paths in both files:

1. `start.sh` — update the `cd` path
2. `~/Library/LaunchAgents/com.mgjc.delivery-tracker.plist` — update `ProgramArguments` and `WorkingDirectory`

Then reload:

```bash
launchctl unload ~/Library/LaunchAgents/com.mgjc.delivery-tracker.plist
launchctl load ~/Library/LaunchAgents/com.mgjc.delivery-tracker.plist
```

---

## Usage

### Creating a Project

1. Click **Projects** in the sidebar and select a project type, or click **View All**.
2. Click **New Project**.
3. Fill in project details: name, customer, scope, project manager, technology, and team members.
4. Select the project type — this determines which KPIs are loaded.
5. Save. All relevant KPIs are automatically created for the project.

### Tracking Metrics

1. Open a project from the project list.
2. Use the **stage tabs** to navigate between delivery stages.
3. Enter metric values (percentages, yes/no, counts, scores) and optional notes.
4. Click **Save** to persist. The stage completion percentage updates automatically.

### Dashboard

The dashboard shows:
- **Summary cards** — total projects, active, completed, on hold
- **Project type distribution** — bar chart
- **Status breakdown** — doughnut chart
- **Stage completion averages** — bar chart across all active projects

### Reference Tab

The reference page has two sections:
- **KPI Summary Slides** — tabbed visual overviews per project type with key targets
- **Detailed KPI Definitions** — expandable accordion tables with full KPI descriptions, measurement formulas, and input types

---

## Updating KPIs

KPI definitions live in `metrics_config.py`. See [METRICS_UPDATE_GUIDE.md](METRICS_UPDATE_GUIDE.md) for step-by-step instructions on how to:

- Add, modify, or remove individual KPIs
- Add or remove delivery stages
- Add entirely new project types
- Map data from the source Excel spreadsheet

**Note:** Changes only affect newly created projects. Existing projects retain the metrics they were created with.

---

## Database

The app uses a file-based SQLite database (`delivery_tracker.db`) that is auto-created on first run. It stores:

- **Projects** — name, customer, scope, PM, technology, type, status
- **Engineers** — team members linked to projects
- **MetricEntries** — KPI values per project per stage

To reset the database completely:

```bash
rm delivery_tracker.db
# Restart the app — a fresh DB is created automatically
```

The database file is excluded from version control via `.gitignore`.

---

## API Endpoints

| Method | Path                              | Description                          |
|--------|-----------------------------------|--------------------------------------|
| GET    | `/`                               | Dashboard                            |
| GET    | `/projects`                       | Project list (supports `?search=`, `?type=`, `?status=`) |
| GET    | `/projects/new`                   | New project form                     |
| POST   | `/projects/new`                   | Create project                       |
| GET    | `/projects/<id>`                  | Project detail (supports `?stage=`)  |
| POST   | `/projects/<id>/metrics`          | Update metrics for a stage           |
| GET    | `/projects/<id>/edit`             | Edit project form                    |
| POST   | `/projects/<id>/edit`             | Save project edits                   |
| POST   | `/projects/<id>/delete`           | Delete project                       |
| GET    | `/reference`                      | KPI reference page                   |
| GET    | `/api/dashboard-data`             | JSON data for dashboard charts       |

---

## License

Internal use — Cisco Confidential.
