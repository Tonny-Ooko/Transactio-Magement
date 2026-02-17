from flask import Flask, request, jsonify
from config import Config
from models import db, Transaction, Payment, MissionGoal
from services import kes_to_usd, categorize

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

    # Ensure one mission row exists
    if not MissionGoal.query.first():
        mission = MissionGoal(
            target_ksh=500000,
            target_usd=3000
        )
        db.session.add(mission)
        db.session.commit()


# -----------------------------
# VALIDATION ENDPOINT
# -----------------------------
@app.route("/mpesa/validation", methods=["POST"])
def validation():
    data = request.get_json()
    amount = float(data.get("TransAmount", 0))

    if amount < 10:
        return jsonify({
            "ResultCode": 1,
            "ResultDesc": "Minimum contribution is 10 KSH"
        })

    return jsonify({
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    })


# -----------------------------
# CONFIRMATION ENDPOINT
# -----------------------------
@app.route("/mpesa/confirmation", methods=["POST"])
def confirmation():
    data = request.get_json()

    trans_id = data.get("TransID")

    # Prevent duplicate transaction
    existing = Transaction.query.filter_by(trans_id=trans_id).first()
    if existing:
        return jsonify({
            "ResultCode": 0,
            "ResultDesc": "Duplicate ignored"
        })

    try:
        amount = float(data.get("TransAmount", 0))
        bill_ref = data.get("BillRefNumber", "")
        category = categorize(bill_ref)
        usd = kes_to_usd(amount)

        # Save raw transaction
        transaction = Transaction(
            trans_id=trans_id,
            phone_number=data.get("MSISDN"),
            first_name=data.get("FirstName"),
            middle_name=data.get("MiddleName"),
            last_name=data.get("LastName"),
            amount=amount,
            bill_ref=bill_ref,
            trans_time=data.get("TransTime")
        )

        db.session.add(transaction)

        # Save accounting payment
        payment = Payment(
            receipt=trans_id,
            phone=data.get("MSISDN"),
            full_name=f"{data.get('FirstName','')} {data.get('LastName','')}",
            amount_ksh=amount,
            amount_usd=usd,
            category=category,
            account_ref=bill_ref
        )

        db.session.add(payment)

        # Update Mission totals if needed
        if category == "MISSION":
            mission = MissionGoal.query.first()
            mission.collected_ksh += amount
            mission.collected_usd += usd

        db.session.commit()

        return jsonify({
            "ResultCode": 0,
            "ResultDesc": "Confirmation received successfully"
        })

    except Exception as e:
        db.session.rollback()
        print("Database Error:", e)

        return jsonify({
            "ResultCode": 1,
            "ResultDesc": "Database error"
        })


if __name__ == "__main__":
    app.run(port=5000, debug=True)
