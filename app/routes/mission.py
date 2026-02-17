from flask import Blueprint, render_template, send_file
from flask_login import login_required
from app.models.mission import MissionGoal
from app.services.pdf_reports import mission_report

mission_bp = Blueprint("mission", __name__, url_prefix="/mission")

@mission_bp.route("/")
def mission():
    mission = MissionGoal.query.first()
    percent = (mission.collected_ksh / mission.target_ksh) * 100
    remaining = 100 - percent
    return render_template(
        "mission.html",
        mission=mission,
        percent=round(percent,2),
        remaining=round(remaining,2)
    )
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