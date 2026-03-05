from flask import Blueprint, render_template, send_file, request, redirect, url_for, flash
from flask_login import login_required
from ..models import MissionGoal
from ..services.pdf_reports import mission_report
from ..extensions import db
from ..services import kes_to_usd



mission_bp = Blueprint("mission", __name__, url_prefix="/mission")



@mission_bp.route("/")
def mission():
    mission = MissionGoal.query.first()

    target = mission.target_ksh if mission else 0
    collected = mission.collected_ksh if mission else 0

    percent = (collected / target * 100) if target else 0
    remaining = 100 - percent

    return render_template(
        "mission.html",
        mission=mission,
        percent=round(percent, 1),
        remaining=round(remaining, 1),
    )

@mission_bp.route("/mission/update", methods=["POST"])
def update_mission():
    mission_id = request.form.get("mission_id")

    mission = MissionGoal.query.get_or_404(mission_id)

    mission.name = request.form.get("name")
    mission.target_ksh = float(request.form.get("target_ksh"))

    # auto compute USD on backend (important fallback)
    mission.target_usd = kes_to_usd(mission.target_ksh)

    db.session.commit()
    flash("Mission updated successfully", "success")

    return redirect(url_for("admin_dashboard"))

@login_required
def mission():
    mission = MissionGoal.query.first()
    return render_template("mission.html", mission=mission)

@mission_bp.route("/report/pdf")
@login_required
def mission_pdf():
    path = "mission_report.pdf"
    mission_report(MissionGoal.query.first(), path)
    return send_file(path, as_attachment=True)