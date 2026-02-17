import requests

def kes_to_usd(amount):
    try:
        r = requests.get("https://api.exchangerate-api.com/v4/latest/KES")
        rate = r.json()["rates"]["USD"]
        return round(amount * rate, 2)
    except:
        return round(amount / 130, 2)
