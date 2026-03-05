import os

class Config:
    # -----------------------------
    # MYSQL DATABASE CONFIG
    # -----------------------------
    DB_USER = "mpesa_user"
    DB_PASSWORD = "StrongPassword123"
    DB_HOST = "localhost"
    DB_NAME = "mpesa_accounting"

    SQLALCHEMY_DATABASE_URI = "postgresql://mpesa_user:StrongPassword123@localhost/mpesa_accounting_db"


    # -----------------------------
    # DAR AJA CONFIG (SANDBOX)
    # -----------------------------
    MPESA_CONSUMER_KEY = "GV4vURSNke8X9xLvNfayUoqxkUv3kQK3lr6UlqEcw2VAUlD4"
    MPESA_CONSUMER_SECRET = "Xz23qQXE06lGXwnOFGL1aFrQDslR1Na6Ea2xAeiG3muGYJHRP09SOLXAwcdw992t"
    MPESA_SHORTCODE = "4224574"

    MPESA_AUTH_URL = "https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    MPESA_REGISTER_URL = "https://api.safaricom.co.ke/mpesa/c2b/v2/registerurl"

    BASE_URL = "https://yourdomain.com"
    CONFIRMATION_URL = f"{BASE_URL}/mpesa/confirmation"
    VALIDATION_URL = f"{BASE_URL}/mpesa/validation"
