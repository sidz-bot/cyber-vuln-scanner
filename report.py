def generate_report(target, services, vulnerabilities):

    print("\n====== SECURITY SCAN REPORT ======")

    print("Target:", target)

    print("\nOpen Services:")

    for s in services:
        print(f"Port {s['port']} - {s['service']}")

    print("\nPossible Vulnerabilities:")

    if vulnerabilities:
        for v in vulnerabilities:
            print(v)
    else:
        print("No obvious vulnerabilities detected")