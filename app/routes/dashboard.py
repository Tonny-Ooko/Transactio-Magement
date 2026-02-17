from flask import Blueprint, render_template
from app.models.payment import Payment
from flask_login import login_required


dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/")
def dashboard():
    payments = Payment.query.order_by(Payment.created_at.desc()).all()
    return render_template("dashboard.html", payments=payments)
@login_required
def dashboard():
    payments = Payment.query.order_by(Payment.created_at.desc()).all()
    return render_template("dashboard.html", payments=payments)