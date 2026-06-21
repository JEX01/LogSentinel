from collections import defaultdict


def detect_password_spraying(failed_attempts, threshold=3):

    ip_users = defaultdict(set)

    for entry in failed_attempts:

        ip_users[entry["ip"]].add(
            entry["user"]
        )

    findings = []

    for ip, users in ip_users.items():

        if len(users) >= threshold:

            findings.append({
                "ip": ip,
                "users_targeted": len(users),
                "accounts": list(users)
            })

    return findings
