import re


def extract_failed_logins(log_file):

    with open(log_file, "r") as file:
        logs = file.readlines()

    failed_attempts = []

    pattern = r"Failed password for (\w+) from (\d+\.\d+\.\d+\.\d+)"

    for line in logs:

        match = re.search(pattern, line)

        if match:

            failed_attempts.append({
                "user": match.group(1),
                "ip": match.group(2)
            })

    return failed_attempts
