import os
from datetime import datetime, timezone

from flask import (
    Flask,
    flash,
    jsonify,
    redirect,
    render_template,
    request,
    url_for,
)

from models import MetricEntry, Project, Engineer, db
from metrics_config import (
    PROJECT_TYPES,
    PROJECT_TYPE_CONFIG,
    get_stages,
    get_stage_metrics,
)

app = Flask(__name__)
app.secret_key = os.urandom(32)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "sqlite:///" + os.path.join(basedir, "delivery_tracker.db")
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.context_processor
def inject_globals():
    type_project_counts = {}
    for pt in PROJECT_TYPES:
        type_project_counts[pt] = Project.query.filter_by(project_type=pt).count()
    return {
        "project_types": PROJECT_TYPES,
        "type_project_counts": type_project_counts,
        "now": datetime.now(timezone.utc),
    }


# ── Dashboard ────────────────────────────────────────────────────────────────

@app.route("/")
def dashboard():
    projects = Project.query.all()
    type_counts = {pt: Project.query.filter_by(project_type=pt).count() for pt in PROJECT_TYPES}

    status_counts = {"Active": 0, "Completed": 0, "On Hold": 0}
    for p in projects:
        status_counts[p.status] = status_counts.get(p.status, 0) + 1

    project_summaries = []
    for p in projects:
        metrics = MetricEntry.query.filter_by(project_id=p.id).all()
        total = len(metrics)
        filled = sum(1 for m in metrics if m.actual_value is not None or m.actual_text)
        pct = round(filled / total * 100) if total else 0
        project_summaries.append({"project": p, "filled": filled, "total": total, "pct": pct})

    project_summaries.sort(key=lambda x: x["pct"], reverse=True)

    return render_template(
        "dashboard.html",
        projects=projects,
        type_counts=type_counts,
        status_counts=status_counts,
        project_summaries=project_summaries,
    )


# ── Projects list ────────────────────────────────────────────────────────────

@app.route("/projects")
def projects():
    search = request.args.get("search", "").strip()
    ptype = request.args.get("type", "").strip()
    status = request.args.get("status", "").strip()

    query = Project.query
    if search:
        like = f"%{search}%"
        query = query.filter(
            db.or_(
                Project.name.ilike(like),
                Project.customer_name.ilike(like),
                Project.project_manager.ilike(like),
                Project.technology.ilike(like),
            )
        )
    if ptype:
        query = query.filter_by(project_type=ptype)
    if status:
        query = query.filter_by(status=status)

    all_projects = query.order_by(Project.updated_at.desc()).all()
    return render_template(
        "projects.html",
        projects=all_projects,
        search=search,
        selected_type=ptype,
        selected_status=status,
    )


# ── Create project ───────────────────────────────────────────────────────────

@app.route("/projects/new", methods=["GET", "POST"])
def new_project():
    if request.method == "POST":
        project = Project(
            name=request.form["name"],
            customer_name=request.form["customer_name"],
            scope=request.form.get("scope", ""),
            project_manager=request.form["project_manager"],
            technology=request.form.get("technology", ""),
            project_type=request.form["project_type"],
            status=request.form.get("status", "Active"),
        )
        db.session.add(project)
        db.session.flush()

        eng_names = request.form.getlist("eng_name[]")
        eng_desigs = request.form.getlist("eng_designation[]")
        for n, d in zip(eng_names, eng_desigs):
            if n.strip():
                db.session.add(
                    Engineer(project_id=project.id, name=n.strip(), designation=d.strip())
                )

        ptype = project.project_type
        for stage_name, stage_metrics in PROJECT_TYPE_CONFIG.get(ptype, []):
            for m in stage_metrics:
                db.session.add(
                    MetricEntry(
                        project_id=project.id,
                        stage=stage_name,
                        kpi_name=m["kpi"],
                        kpi_detail=m.get("kpi_detail", ""),
                        metric_formula=m.get("metric", ""),
                        input_type=m.get("input_type", "percentage"),
                    )
                )

        db.session.commit()
        flash(f'Project "{project.name}" created successfully.', "success")
        return redirect(url_for("project_detail", project_id=project.id))

    return render_template("project_form.html", project=None)


# ── Project detail ───────────────────────────────────────────────────────────

@app.route("/projects/<int:project_id>")
def project_detail(project_id):
    project = Project.query.get_or_404(project_id)
    stages = get_stages(project.project_type)

    metrics_by_stage = {}
    for stage in stages:
        metrics_by_stage[stage] = (
            MetricEntry.query.filter_by(project_id=project.id, stage=stage)
            .order_by(MetricEntry.id)
            .all()
        )

    stage_progress = {}
    for stage, metrics in metrics_by_stage.items():
        total = len(metrics)
        filled = sum(1 for m in metrics if m.actual_value is not None or m.actual_text)
        stage_progress[stage] = round(filled / total * 100) if total else 0

    active_stage = request.args.get("stage", stages[0] if stages else "")

    return render_template(
        "project_detail.html",
        project=project,
        stages=stages,
        metrics_by_stage=metrics_by_stage,
        stage_progress=stage_progress,
        active_stage=active_stage,
    )


# ── Update metrics ───────────────────────────────────────────────────────────

@app.route("/projects/<int:project_id>/metrics", methods=["POST"])
def update_metrics(project_id):
    project = Project.query.get_or_404(project_id)
    stage = request.form.get("stage", "")

    metrics = MetricEntry.query.filter_by(project_id=project.id, stage=stage).all()
    for m in metrics:
        if m.input_type == "yes_no":
            m.actual_text = request.form.get(f"actual_{m.id}", "").strip() or None
            m.actual_value = None
        else:
            field_val = request.form.get(f"actual_{m.id}", "").strip()
            if field_val:
                try:
                    m.actual_value = float(field_val)
                except ValueError:
                    pass
            else:
                m.actual_value = None
            m.actual_text = None

        m.notes = request.form.get(f"notes_{m.id}", "").strip()
        m.updated_at = datetime.now(timezone.utc)

    db.session.commit()
    flash(f'Metrics for "{stage}" updated.', "success")
    return redirect(url_for("project_detail", project_id=project.id, stage=stage))


# ── Edit project ─────────────────────────────────────────────────────────────

@app.route("/projects/<int:project_id>/edit", methods=["GET", "POST"])
def edit_project(project_id):
    project = Project.query.get_or_404(project_id)

    if request.method == "POST":
        project.name = request.form["name"]
        project.customer_name = request.form["customer_name"]
        project.scope = request.form.get("scope", "")
        project.project_manager = request.form["project_manager"]
        project.technology = request.form.get("technology", "")
        project.status = request.form.get("status", project.status)

        Engineer.query.filter_by(project_id=project.id).delete()
        eng_names = request.form.getlist("eng_name[]")
        eng_desigs = request.form.getlist("eng_designation[]")
        for n, d in zip(eng_names, eng_desigs):
            if n.strip():
                db.session.add(
                    Engineer(project_id=project.id, name=n.strip(), designation=d.strip())
                )

        db.session.commit()
        flash(f'Project "{project.name}" updated.', "success")
        return redirect(url_for("project_detail", project_id=project.id))

    return render_template("project_form.html", project=project)


# ── Delete project ───────────────────────────────────────────────────────────

@app.route("/projects/<int:project_id>/delete", methods=["POST"])
def delete_project(project_id):
    project = Project.query.get_or_404(project_id)
    name = project.name
    db.session.delete(project)
    db.session.commit()
    flash(f'Project "{name}" deleted.', "success")
    return redirect(url_for("projects"))


# ── Reference ────────────────────────────────────────────────────────────────

@app.route("/reference")
def reference():
    return render_template("reference.html", config=PROJECT_TYPE_CONFIG)


# ── Dashboard API ────────────────────────────────────────────────────────────

@app.route("/api/dashboard-data")
def dashboard_data():
    type_counts = {pt: Project.query.filter_by(project_type=pt).count() for pt in PROJECT_TYPES}

    status_counts = {}
    for s in ["Active", "Completed", "On Hold"]:
        status_counts[s] = Project.query.filter_by(status=s).count()

    stage_completion = {}
    for p in Project.query.filter_by(status="Active").all():
        stages = get_stages(p.project_type)
        for stage in stages:
            metrics = MetricEntry.query.filter_by(project_id=p.id, stage=stage).all()
            total = len(metrics)
            filled = sum(1 for m in metrics if m.actual_value is not None or m.actual_text)
            pct = round(filled / total * 100) if total else 0
            stage_completion.setdefault(stage, []).append(pct)

    stage_avg = {}
    for stage, vals in stage_completion.items():
        stage_avg[stage] = round(sum(vals) / len(vals)) if vals else 0

    return jsonify({
        "type_counts": type_counts,
        "status_counts": status_counts,
        "stage_averages": stage_avg,
    })


if __name__ == "__main__":
    app.run(debug=True, port=5050)
