import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():

    with open(
        "reports/threat_scores.json",
        "r"
    ) as file:
        attacks = json.load(file)

    total_attacks = len(attacks)

    critical = sum(
        1
        for attack in attacks
        if attack["score"] >= 80
    )

    return render_template(
        "index.html",
        attacks=attacks,
        total_attacks=total_attacks,
        critical=critical
    )


if __name__ == "__main__":
    app.run(debug=True)
