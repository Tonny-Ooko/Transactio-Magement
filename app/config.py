import os

class Config:
    # -----------------------------
    # MYSQL DATABASE CONFIG
    # -----------------------------
    DB_USER = "mpesa_user"
    DB_PASSWORD = ""
    DB_HOST = "localhost"
    DB_NAME = "mpesa_accounting"

    SQLALCHEMY_DATABASE_URI = (
        f"mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # -----------------------------
    # DAR AJA CONFIG (SANDBOX)
    # -----------------------------
    MPESA_CONSUMER_KEY = "GV4vURSNke8XqEcw2VAUlD4"
    MPESA_CONSUMER_SECRET = "Xz23qQXE06lGXwnOFGL2t"
    MPESA_SHORTCODE = ""

    MPESA_AUTH_URL = "https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    MPESA_REGISTER_URL = "https://api.safaricom.co.ke/mpesa/c2b/v2/registerurl"

    BASE_URL = "https://yourdomain.com"
    CONFIRMATION_URL = f"{BASE_URL}/mpesa/confirmation"
    VALIDATION_URL = f"{BASE_URL}/mpesa/validation"
