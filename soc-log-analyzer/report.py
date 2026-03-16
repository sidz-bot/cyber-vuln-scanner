def generate_report(data):

    with open("security_report.txt", "w") as report:

        report.write("SOC SECURITY INCIDENT REPORT\n")
        report.write("============================\n\n")

        for ip, info in data.items():

            report.write(f"IP Address: {ip}\n")
            report.write(f"Failed Attempts: {info['attempts']}\n")
            report.write(f"Severity Level: {info['severity']}\n")
            report.write("-----------------------------\n")

    print("\n📄 Security report generated: security_report.txt")