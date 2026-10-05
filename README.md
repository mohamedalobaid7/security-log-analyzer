# Security Log Analyzer

A Flask-based cybersecurity project designed to analyze login activity and detect suspicious authentication behavior.

# Features

- Detects late-night successful login activity.
- Detects possible brute-force attacks.
- Identifies 5 or more failed login attempts from the same IP within a 10-minute window.
- Displays login events and security alerts through a cybersecurity-themed dashboard.
- Shows IP addresses, usernames, timestamps, login status, and threat severity.

# Technologies Used

- Python
- Flask
- HTML
- CSS
- Jinja2
- Git & GitHub

## Detection Logic

### Late-Night Login Detection
Successful login attempts occurring between 12:00 AM and 5:00 AM are flagged as suspicious.

### Brute Force Detection
An alert is generated when the same IP address produces 5 or more failed login attempts within a 10-minute period.

## Project Structure

text
security-log-analyzer/
│
├── app.py
├── sample_logs.txt
├── requirements.txt
├── .gitignore
│
└── templates/
    └── index.html
