import re


def parse_apache_log(log_file):

    with open(log_file, "r") as file:
        logs = file.readlines()

    parsed_logs = []

    for line in logs:

        ip_match = re.search(r"(\d+\.\d+\.\d+\.\d+)", line)

        if ip_match:

            parsed_logs.append({
                "ip": ip_match.group(1),
                "line": line.strip()
            })

    return parsed_logs
