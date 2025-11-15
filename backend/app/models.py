from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Department(db.Model):
    __tablename__ = "departments"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.Text)

    users = db.relationship("User", backref="department", lazy=True)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # 'admin' or 'employee'
    department_id = db.Column(db.Integer, db.ForeignKey("departments.id"))
    designation = db.Column(db.String(150))
    base_salary = db.Column(db.Numeric(10, 2))
    status = db.Column(db.String(20), default="active")
    qr_secret = db.Column(db.String(64), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

class AttendanceRecord(db.Model):
    __tablename__ = "attendance_records"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    date = db.Column(db.Date, nullable=False)
    check_in_time = db.Column(db.Time)
    check_out_time = db.Column(db.Time)
    status = db.Column(db.String(20), default="present")
    source = db.Column(db.String(20), default="qr")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class PayrollRun(db.Model):
    __tablename__ = "payroll_runs"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    month = db.Column(db.Integer, nullable=False)
    base_salary = db.Column(db.Numeric(10, 2))
    working_days = db.Column(db.Integer)
    present_days = db.Column(db.Integer)
    gross_pay = db.Column(db.Numeric(10, 2))
    deductions = db.Column(db.Numeric(10, 2))
    net_pay = db.Column(db.Numeric(10, 2))
    generated_at = db.Column(db.DateTime, default=datetime.utcnow)
