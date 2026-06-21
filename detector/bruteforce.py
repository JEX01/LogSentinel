from collections import Counter


def get_risk_level(attempts):

    if attempts >= 20:
        return "CRITICAL"

    elif attempts >= 10:
        return "HIGH"

    elif attempts >= 5:
        return "MEDIUM"

    return "LOW"


def detect_bruteforce(failed_attempts, threshold=3):

    ips = [entry["ip"] for entry in failed_attempts]

    counter = Counter(ips)

    suspicious = []

    for ip, count in counter.items():

        if count >= threshold:

            suspicious.append({
                "ip": ip,
                "attempts": count,
                "risk": get_risk_level(count)
            })

    return suspicious
