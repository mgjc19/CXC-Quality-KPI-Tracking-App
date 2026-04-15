from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Project(db.Model):
    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    customer_name = db.Column(db.String(200), nullable=False)
    scope = db.Column(db.Text)
    project_manager = db.Column(db.String(200), nullable=False)
    technology = db.Column(db.String(300))
    project_type = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), default="Active")
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    engineers = db.relationship(
        "Engineer", backref="project", cascade="all, delete-orphan", lazy=True
    )
    metrics = db.relationship(
        "MetricEntry", backref="project", cascade="all, delete-orphan", lazy=True
    )


class Engineer(db.Model):
    __tablename__ = "engineers"

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey("projects.id"), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    designation = db.Column(db.String(200), nullable=False)


class MetricEntry(db.Model):
    __tablename__ = "metric_entries"

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey("projects.id"), nullable=False)
    stage = db.Column(db.String(100), nullable=False)
    kpi_name = db.Column(db.String(300), nullable=False)
    kpi_detail = db.Column(db.Text)
    metric_formula = db.Column(db.Text)
    input_type = db.Column(db.String(20), default="percentage")
    actual_value = db.Column(db.Float)
    actual_text = db.Column(db.String(50))
    notes = db.Column(db.Text)
    updated_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    __table_args__ = (
        db.UniqueConstraint("project_id", "stage", "kpi_name", name="uq_metric"),
    )

    @property
    def display_value(self):
        if self.input_type == "yes_no":
            return self.actual_text or "—"
        if self.actual_value is not None:
            if self.input_type == "percentage":
                return f"{self.actual_value}%"
            return str(self.actual_value)
        return "—"

    @property
    def health(self):
        if self.input_type == "yes_no":
            if not self.actual_text:
                return "not_started"
            return "on_track" if self.actual_text == "Yes" else "at_risk"
        if self.actual_value is None:
            return "not_started"
        return "entered"
