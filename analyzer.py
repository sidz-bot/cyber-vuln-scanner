def analyze_services(services):

    vulnerabilities = []

    for service in services:

        if service["service"] == "ssh":
            vulnerabilities.append(
                f"Port {service['port']} → SSH detected (Possible brute force risk)"
            )

        elif service["service"] == "ftp":
            vulnerabilities.append(
                f"Port {service['port']} → FTP detected (Anonymous login risk)"
            )

        elif service["service"] == "http":
            vulnerabilities.append(
                f"Port {service['port']} → Web server detected (Check OWASP vulnerabilities)"
            )

    return vulnerabilities