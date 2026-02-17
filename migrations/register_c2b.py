import requests
from requests.auth import HTTPBasicAuth
from config import Config


def get_access_token():
    response = requests.get(
        Config.MPESA_AUTH_URL,
        auth=HTTPBasicAuth(
            Config.MPESA_CONSUMER_KEY,
            Config.MPESA_CONSUMER_SECRET
        )
    )
    return response.json()["access_token"]


def register():
    token = get_access_token()

    headers = {
        "Authorization": f"Bearer {token}"
    }

    payload = {
        "ShortCode": Config.MPESA_SHORTCODE,
        "ResponseType": "Completed",
        "ConfirmationURL": Config.CONFIRMATION_URL,
        "ValidationURL": Config.VALIDATION_URL
    }

    response = requests.post(
        Config.MPESA_REGISTER_URL,
        json=payload,
        headers=headers
    )

    print("Registration Response:")
    print(response.json())


if __name__ == "__main__":
    register()
