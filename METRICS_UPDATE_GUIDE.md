# How to Update Metrics & KPIs

This guide explains how to manually update the delivery quality metrics and KPIs when the source Excel file (`PSTG Quality metrics.xlsx`) is modified.

---

## Overview

All metric definitions live in a single file:

```
metrics_config.py
```

This file contains the KPIs and metrics for all 5 project types. When you update the Excel, you need to mirror those changes in this Python file.

**Important:** Changes to `metrics_config.py` only affect **newly created projects**. Existing projects retain the metrics they were created with. If you need to update metrics on an existing project, you must delete and recreate it.

---

## File Structure

The `metrics_config.py` file is organized as follows:

```
PROJECT_TYPES           → List of project type names (displayed in sidebar)
_MATURED_PDI            → Metrics for "Matured PDI" projects
_EMERGING_PDI           → Metrics for "Emerging PDI" projects
_BF_TRANSFORMATION      → Metrics for "Brown Field Transformation" projects
_MIGRATION              → Metrics for "Migration" projects
_UPGRADE                → Metrics for "Upgrade" projects
PROJECT_TYPE_CONFIG     → Master dictionary linking names to their config
```

Each project type variable (e.g., `_MATURED_PDI`) is a **list of tuples**, where each tuple is:

```python
("Stage Name", [list of metric dictionaries])
```

Each metric dictionary has these fields:

| Field         | Required | Description                                      |
|---------------|----------|--------------------------------------------------|
| `kpi`         | Yes      | Short display name for the KPI                   |
| `kpi_detail`  | Yes      | Full description (shown when user clicks info icon) |
| `metric`      | Yes      | The measurement formula or definition            |
| `input_type`  | Yes      | One of: `percentage`, `yes_no`, `count`, `number`, `score` |

---

## Step-by-Step: Adding a New KPI to an Existing Stage

**Example:** Adding a new KPI "Customer Feedback Score" to the "Post Implementation" stage of Matured PDI.

1. Open `metrics_config.py` in any text editor.

2. Find the `_MATURED_PDI` variable.

3. Locate the `"Post Implementation"` stage tuple.

4. Add a new dictionary to the list:

```python
("Post Implementation", [
    # ... existing metrics ...
    {
        "kpi": "Customer Feedback Score",
        "kpi_detail": "Rating from customer feedback survey post-implementation.",
        "metric": "Score on a scale of 1-10",
        "input_type": "score",
    },
]),
```

5. Save the file. The app auto-reloads (debug mode).

---

## Step-by-Step: Adding a New Stage

**Example:** Adding a "Pilot Phase" stage to Migration projects.

1. Open `metrics_config.py`.

2. Find the `_MIGRATION` variable.

3. Add a new tuple at the desired position in the list (stages appear in order):

```python
_MIGRATION = [
    ("Pre Engagement", [...]),
    ("Migration Approach Planning", [...]),
    ("Pilot Phase", [                          # ← New stage
        {
            "kpi": "Pilot Scope Coverage",
            "kpi_detail": "Percentage of scope covered in the pilot.",
            "metric": "(Pilot scope items / Total scope items) × 100%",
            "input_type": "percentage",
        },
        {
            "kpi": "Pilot Sign-off",
            "kpi_detail": "Whether the pilot has been signed off by customer.",
            "metric": "Yes/No",
            "input_type": "yes_no",
        },
    ]),
    ("Migration Plan", [...]),
    # ... rest of stages ...
]
```

4. Save the file.

---

## Step-by-Step: Modifying an Existing KPI

1. Open `metrics_config.py`.

2. Find the project type and stage.

3. Locate the metric dictionary by its `kpi` field.

4. Edit the fields you need to change (name, description, formula, or input type).

5. Save the file.

**Example:** Changing the metric formula text:

```python
# Before
"metric": "Yes/No",

# After
"metric": "Yes/No (No is a risk — requires immediate escalation)",
```

---

## Step-by-Step: Removing a KPI

1. Open `metrics_config.py`.

2. Find the metric dictionary.

3. Delete the entire dictionary block (including the curly braces and trailing comma).

4. Save the file.

---

## Step-by-Step: Adding a New Project Type

1. Create a new variable at the module level:

```python
_NEW_TYPE = [
    ("Stage 1", [
        {"kpi": "...", "kpi_detail": "...", "metric": "...", "input_type": "percentage"},
    ]),
    ("Stage 2", [
        {"kpi": "...", "kpi_detail": "...", "metric": "...", "input_type": "yes_no"},
    ]),
]
```

2. Add the type name to `PROJECT_TYPES`:

```python
PROJECT_TYPES = [
    "Matured PDI",
    "Emerging PDI",
    "Brown Field Transformation",
    "Migration",
    "Upgrade",
    "New Type Name",           # ← Add here
]
```

3. Add the mapping to `PROJECT_TYPE_CONFIG`:

```python
PROJECT_TYPE_CONFIG = {
    # ... existing entries ...
    "New Type Name": _NEW_TYPE,   # ← Add here
}
```

4. Save the file.

---

## Input Type Reference

| `input_type`  | UI Element        | When to Use                                         |
|---------------|-------------------|-----------------------------------------------------|
| `percentage`  | Number input (%)  | Formula-based metrics returning a percentage        |
| `yes_no`      | Yes/No dropdown   | Compliance/readiness checks                         |
| `count`       | Number input (#)  | Counting items (escalations, defects, etc.)         |
| `number`      | Number input      | Numeric values that aren't percentages (e.g., avg review cycles) |
| `score`       | Number input      | Scores like CSAT                                    |

---

## After Making Changes

1. **Save `metrics_config.py`** — if the app is running in debug mode, it auto-reloads.

2. **If the app is not running**, start it:
   ```bash
   cd "/Users/mgjc/Desktop/Projects/AI/CXC-Quality-KPI-Tracking-App"
   ./start.sh
   ```

3. **Verify** by going to the **References** page (`http://127.0.0.1:5050/reference`) — all metrics are listed there.

4. **Create a new project** of the relevant type to confirm the new/updated metrics appear correctly.

5. **Existing projects are not affected** — they keep whatever metrics they were created with.

---

## Database Reset (if needed)

If you want a completely fresh start (removes all projects and data):

```bash
rm delivery_tracker.db
```

The database is automatically recreated when the app starts.

---

## Mapping Excel to Config

When reading the Excel file, map the columns as follows:

| Excel Column | Config Field   |
|-------------|----------------|
| Column A (Stages) | Stage name in the tuple: `("Stage Name", [...])` |
| Column B (KPI)    | `kpi` (short name) and `kpi_detail` (full text) |
| Column C (Metrics)| `metric` field |
| Inferred from Column C | `input_type` — see rules below |

**How to determine `input_type` from the Metrics column:**

- Contains `× 100%` or `× 100` or mentions percentage → `percentage`
- Says `Yes/No` → `yes_no`
- Says `# Number` or is a count → `count`
- Says `CSAT` or is a rating → `score`
- Says `Average #` or `<=2` (numeric threshold) → `number`
- Contains `hours saving` or `hours/hours` ratios → `percentage`
