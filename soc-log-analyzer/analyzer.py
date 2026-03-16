from collections import defaultdict
import report

log_file = "sample_logs.txt"

failed_attempts = defaultdict(int)
suspicious_ips = {}

with open(log_file, "r") as file:
    for line in file:
        if "Failed login" in line:
            ip = line.strip().split()[-1]
            failed_attempts[ip] += 1

print("\n🔎 SOC Log Analyzer Running...\n")

for ip, count in failed_attempts.items():

    if count >= 5:
        severity = "HIGH"
    elif count >= 3:
        severity = "MEDIUM"
    else:
        severity = "LOW"

    if count >= 3:
        suspicious_ips[ip] = {
            "attempts": count,
            "severity": severity
        }

        print(f"🚨 ALERT DETECTED")
        print(f"IP Address: {ip}")
        print(f"Failed Attempts: {count}")
        print(f"Severity: {severity}\n")

print("📊 Analysis Complete")

report.generate_report(suspicious_ips)