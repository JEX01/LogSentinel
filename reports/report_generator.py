import csv


def generate_csv(results, filename="reports/security_report.csv"):

    with open(filename, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "IP Address",
            "Failed Attempts",
            "Risk Level"
        ])

        for item in results:

            writer.writerow([
                item["ip"],
                item["attempts"],
                item["risk"]
            ])

    print(f"\nReport saved to {filename}")
