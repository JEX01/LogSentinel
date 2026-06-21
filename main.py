from parser.auth_parser import extract_failed_logins
from parser.apache_parser import parse_apache_log

from detector.bruteforce import detect_bruteforce
from detector.password_spraying import detect_password_spraying
from detector.web_attacks import detect_web_attacks

from detector.geoip import get_ip_info

from detector.threat_score import (
    calculate_threat_scores,
    classify_risk,
    get_top_attackers
)

from detector.geoip import (
    get_ip_info,
    get_country_risk
)

from reports.report_generator import generate_csv


# ---------------------------
# AUTH LOG ANALYSIS
# ---------------------------

failed_attempts = extract_failed_logins(
    "logs/auth.log"
)

results = detect_bruteforce(
    failed_attempts
)

print("\n=== SECURITY REPORT ===\n")

for item in results:
    print(
        f"IP: {item['ip']} | "
        f"Attempts: {item['attempts']} | "
        f"Risk: {item['risk']}"
    )

generate_csv(results)


# ---------------------------
# PASSWORD SPRAYING
# ---------------------------

print("\n=== PASSWORD SPRAYING ===\n")

spray_results = detect_password_spraying(
    failed_attempts
)

for attack in spray_results:

    print(
        f"IP: {attack['ip']} | "
        f"Users Targeted: "
        f"{attack['users_targeted']}"
    )

    print(
        f"Accounts: "
        f"{', '.join(attack['accounts'])}"
    )

    print()


# ---------------------------
# APACHE LOG ANALYSIS
# ---------------------------

print("\n=== WEB ATTACK ANALYSIS ===\n")

apache_logs = parse_apache_log(
    "logs/apache.log"
)

web_findings = detect_web_attacks(
    apache_logs
)

for attack in web_findings:
    print(
        f"IP: {attack['ip']} | "
        f"Type: {attack['type']} | "
        f"Target: {attack['path']}"
    )


# ---------------------------
# THREAT SCORING
# ---------------------------

print("\n=== THREAT SCORES ===\n")

scores = calculate_threat_scores(
    results,
    web_findings,
    spray_results
)

for ip, score in scores.items():

    risk = classify_risk(score)

    print(
        f"IP: {ip} | "
        f"Score: {score} | "
        f"Risk Level: {risk}"
    )

import json

data = []

for ip, score in scores.items():

    data.append({
        "ip": ip,
        "score": score
    })

with open(
    "reports/threat_scores.json",
    "w"
) as file:

    json.dump(
        data,
        file,
        indent=4
    )

# ---------------------------
# TOP ATTACKERS
# ---------------------------

print("\n=== TOP ATTACKERS ===\n")

top_attackers = get_top_attackers(
    scores
)

for rank, (ip, score) in enumerate(
    top_attackers,
    start=1
):

    print(
        f"{rank}. {ip} | "
        f"Score: {score}"
    )

# ---------------------------
# GEOIP INTELLIGENCE
# ---------------------------

print("\n=== GEOIP INTELLIGENCE ===\n")

for ip, score in top_attackers:

    info = get_ip_info(ip)

    risk = get_country_risk(
        info["country"]
    )

    print(
        f"IP: {info['ip']}"
    )

    print(
        f"Country: {info['country']}"
    )

    print(
        f"City: {info['city']}"
    )

    print(
        f"ISP: {info['isp']}"
    )

    print(
        f"Org: {info['org']}"
    )

    print(
        f"Country Risk: {risk}"
    )

    print(
        f"Threat Score: {score}"
    )

    print("-" * 40)

