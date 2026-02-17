from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def mission_report(mission, filepath):
    c = canvas.Canvas(filepath, pagesize=A4)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 800, "Mission Contribution Report")

    c.setFont("Helvetica", 12)
    c.drawString(50, 760, f"Target (KES): {mission.target_ksh}")
    c.drawString(50, 730, f"Collected (KES): {mission.collected_ksh}")

    percent = (mission.collected_ksh / mission.target_ksh) * 100
    c.drawString(50, 700, f"Progress: {round(percent,2)}%")

    c.save()
