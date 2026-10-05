from flask import Flask, render_template
from datetime import datetime, timedelta

app = Flask(__name__)
def read_logs():

    logs = []

    with open("sample_logs.txt", "r") as file:

        for line in file:

            parts = line.strip().split(",")

            timestamp = parts[0]
            ip_address = parts[1]
            username = parts[2]
            status = parts[3]

            logs.append({
                "timestamp": timestamp,
                "ip": ip_address,
                "username": username,
                "status": status
            })

    return logs
def detect_late_night_logins(logs):

    suspicious_logins = []

    for log in logs:

        timestamp = datetime.strptime(
            log["timestamp"],
            "%Y-%m-%d %H:%M:%S"
        )

        hour = timestamp.hour

        if log["status"] == "SUCCESS" and 0 <= hour < 5:

            suspicious_logins.append(log)

    return suspicious_logins
def detect_brute_force(logs):

    failed_logins = {}

    alerts = []

    for log in logs:

        if log["status"] == "FAILED":

            ip = log["ip"]

            timestamp = datetime.strptime(
                log["timestamp"],
                "%Y-%m-%d %H:%M:%S"
            )

            if ip not in failed_logins:
                failed_logins[ip] = []

            failed_logins[ip].append(timestamp)

    for ip, timestamps in failed_logins.items():

        timestamps.sort()

        for start_time in timestamps:

            end_time = start_time + timedelta(minutes=10)

            attempts = 0

            for login_time in timestamps:

                if start_time <= login_time <= end_time:
                    attempts += 1

            if attempts >= 5:

                alerts.append({
                    "ip": ip,
                    "attempts": attempts,
                    "start_time": start_time
                })

                break

    return alerts        

@app.route("/")
def home():

    logs = read_logs()

    late_night_logins = detect_late_night_logins(logs)

    brute_force_alerts = detect_brute_force(logs)

    return render_template(
    "index.html",
    logs=logs,
    late_night_logins=late_night_logins,
    brute_force_alerts=brute_force_alerts
)


if __name__ == "__main__":
    app.run(debug=True)