from detector.geoip import (
    get_ip_info,
    get_country_risk
)


def calculate_threat_scores(
    bruteforce_results,
    web_findings,
    spray_results
):

    scores = {}

    # SSH Bruteforce Scores
    for item in bruteforce_results:

        ip = item["ip"]
        score = item["attempts"] * 2

        if ip not in scores:
            scores[ip] = 0

        scores[ip] += score

    # Web Attack Scores
    for attack in web_findings:

        ip = attack["ip"]

        if ip not in scores:
            scores[ip] = 0

        if attack["type"] == "Sensitive Path Scan":
            scores[ip] += 15

        elif attack["type"] == "SQL Injection Attempt":
            scores[ip] += 40

    # Password Spray Scores
    for spray in spray_results:

        ip = spray["ip"]

        if ip not in scores:
            scores[ip] = 0

        scores[ip] += (
            spray["users_targeted"] * 10
        )

    # GeoIP Intelligence Scores
    for ip in scores:

        info = get_ip_info(ip)

        if get_country_risk(
            info["country"]
        ) == "HIGH":

            scores[ip] += 20

    return scores


def classify_risk(score):

    if score >= 80:
        return "CRITICAL"

    elif score >= 50:
        return "HIGH"

    elif score >= 20:
        return "MEDIUM"

    return "LOW"


def get_top_attackers(scores):

    return sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )
