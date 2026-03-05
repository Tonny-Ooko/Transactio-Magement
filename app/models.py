from datetime import datetime
from flask_login import UserMixin
from .extensions import db




class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), default="accountant")
# -----------------------------
# MPESA TRANSACTIONS
# -----------------------------
class Transaction(db.Model):
    __tablename__ = "transactions"
    id = db.Column(db.Integer, primary_key=True)
    trans_id = db.Column(db.String(50), unique=True, nullable=False)
    phone_number = db.Column(db.String(20))
    first_name = db.Column(db.String(50))
    middle_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    amount = db.Column(db.Float)
    bill_ref = db.Column(db.String(100))
    trans_time = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


# -----------------------------
# ACCOUNTING PAYMENTS
# -----------------------------
class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    receipt = db.Column(db.String(50), unique=True)
    phone = db.Column(db.String(20))
    full_name = db.Column(db.String(100))
    amount_ksh = db.Column(db.Float)
    amount_usd = db.Column(db.Float)
    category = db.Column(db.String(50))
    account_ref = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


# -----------------------------
# MISSION GOAL TRACKER
# -----------------------------
class MissionGoal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    target_ksh = db.Column(db.Float, default=0)
    target_usd = db.Column(db.Float, default=0)
    collected_ksh = db.Column(db.Float, default=0)
    collected_usd = db.Column(db.Float, default=0)
