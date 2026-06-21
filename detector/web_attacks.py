from collections import Counter


SUSPICIOUS_PATHS = [
    "/admin",
    "/wp-admin",
    "/phpmyadmin",
    "/login.php"
]


def detect_web_attacks(logs):

    findings = []

    for log in logs:

        line = log["line"]

        for path in SUSPICIOUS_PATHS:

            if path.lower() in line.lower():

                findings.append({
                    "ip": log["ip"],
                    "type": "Sensitive Path Scan",
                    "path": path
                })

        if "' OR '1'='1" in line:

            findings.append({
                "ip": log["ip"],
                "type": "SQL Injection Attempt",
                "path": "SQLi"
            })

    return findings
