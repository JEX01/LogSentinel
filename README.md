# 🛡️ LogSentinel

### Advanced Security Log Analyzer & Threat Detection Platform

LogSentinel is a Python-based cybersecurity monitoring platform that analyzes Linux authentication logs and Apache web logs to detect malicious activity. It identifies brute-force attacks, password spraying, web reconnaissance, SQL injection attempts, and enriches attacker information using GeoIP intelligence. The platform generates reports, calculates threat scores, and visualizes findings through a Flask dashboard.

---

# 🚀 Features

## Authentication Log Analysis

* Failed Login Detection
* Successful Login Detection
* SSH Brute Force Detection
* Password Spraying Detection

## Apache Log Analysis

* Admin Panel Enumeration Detection
* WordPress Enumeration Detection
* phpMyAdmin Scan Detection
* SQL Injection Detection

## Threat Intelligence

* GeoIP Lookup
* Country Detection
* ISP Detection
* Organization Detection

## Threat Scoring

* Risk Classification
* Attacker Ranking
* Threat Correlation

## Reporting

* CSV Report Generation
* JSON Threat Reports

## Dashboard

* Flask Web Dashboard
* Threat Statistics
* Top Attackers
* Threat Score Charts

---

# 📂 Project Architecture

```text
LogSentinel/
├── dashboard/
│   ├── app.py
│   └── templates/
├── detector/
├── logs/
├── parser/
├── reports/
├── requirements.txt
└── main.py
```

---

# 🛠️ Technologies Used

| Technology | Purpose            |
| ---------- | ------------------ |
| Python     | Core Development   |
| Flask      | Web Dashboard      |
| Regex      | Log Parsing        |
| Requests   | GeoIP Intelligence |
| JSON       | Data Storage       |
| CSV        | Report Generation  |

---

# 🎯 Detection Capabilities

| Threat                | Supported |
| --------------------- | --------- |
| SSH Brute Force       | ✅         |
| Password Spraying     | ✅         |
| SQL Injection         | ✅         |
| Directory Enumeration | ✅         |
| Admin Panel Scanning  | ✅         |
| GeoIP Enrichment      | ✅         |

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/LogSentinel.git
cd LogSentinel
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 📄 Sample Logs vs Your Own Logs

The repository includes sample logs so the project can be tested immediately.

```text
logs/
├── auth.log
└── apache.log
```

These logs contain simulated:

* SSH Brute Force Attacks
* Password Spraying Attacks
* Admin Panel Enumeration
* SQL Injection Attempts

## Run Using Sample Logs

```bash
python3 main.py
```

## Analyze Your Own Logs

Replace the sample files with your own logs:

```text
logs/auth.log
logs/apache.log
```

Or modify the paths inside `main.py`.

Examples:

```text
/var/log/auth.log
/var/log/apache2/access.log
```

Then run:

```bash
python3 main.py
```

---

# ▶️ Running the Analyzer

```bash
python3 main.py
```

Example Output:

```text
=== SECURITY REPORT ===

IP: 10.10.10.50
Attempts: 25
Risk: HIGH

=== PASSWORD SPRAYING ===

IP: 10.10.10.50
Users Targeted: 5

=== THREAT SCORING ===

IP: 10.10.10.50
Score: 120
Risk: CRITICAL
```

Generated Reports:

```text
reports/
├── security_report.csv
└── threat_scores.json
```

---

# 🌐 Running the Dashboard

Start the Flask dashboard:

```bash
python3 dashboard/app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

Dashboard Features:

* Threat Statistics
* Top Attackers
* Threat Score Visualization
* Security Event Monitoring

---

# 📊 Sample Reports

## CSV Report

```csv
IP Address,Failed Attempts,Risk Level
10.10.10.50,25,HIGH
```

## JSON Report

```json
[
    {
        "ip": "10.10.10.50",
        "score": 120
    }
]
```

---

# 🔄 Detection Workflow

```text
Logs
 ↓
Parsers
 ↓
Detectors
 ↓
Threat Scoring
 ↓
Reports
 ↓
Dashboard
```

---

# 📈 Future Improvements

* SQLite Database Integration
* Docker Deployment
* Email Alerting System
* REST API Endpoints
* Threat Intelligence Feeds
* Real-Time Log Monitoring
* User Authentication
* SIEM Integration

---

# 💼 Resume Description

**LogSentinel – Advanced Security Log Analyzer**

Developed a Python-based security monitoring platform capable of analyzing Linux authentication and Apache web logs to detect brute-force attacks, password spraying, web reconnaissance, and SQL injection attempts. Implemented GeoIP threat intelligence, automated threat scoring, CSV/JSON reporting, and a Flask dashboard for real-time visualization of security events and attacker activity.

---

# 📸 Screenshots

```text
screenshots/
├── dashboard.png
├── report.png
└── threat-analysis.png
```

Add screenshots after deployment to demonstrate functionality and improve project presentation.

---

# 👨‍💻 Author

**Your Name**

GitHub: https://github.com/yourusername

LinkedIn: https://linkedin.com/in/yourprofile

---

⭐ If you found this project useful, consider starring the repository.
