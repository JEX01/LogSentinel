import requests


def get_ip_info(ip):

    try:

        response = requests.get(
            f"http://ip-api.com/json/{ip}",
            timeout=5
        )

        data = response.json()

        return {
            "ip": ip,
            "country": data.get("country", "Unknown"),
            "city": data.get("city", "Unknown"),
            "isp": data.get("isp", "Unknown"),
            "org": data.get("org", "Unknown")
        }

    except Exception:

        return {
            "ip": ip,
            "country": "Unknown",
            "city": "Unknown",
            "isp": "Unknown",
            "org": "Unknown"
        }


HIGH_RISK_COUNTRIES = [
    "Russia",
    "North Korea",
    "Iran"
]


def get_country_risk(country):

    if country in HIGH_RISK_COUNTRIES:
        return "HIGH"

    return "NORMAL"
