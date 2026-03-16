import nmap

def scan_target(target):

    nm = nmap.PortScanner()
    nm.scan(target, arguments='-sV')

    services = []

    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            ports = nm[host][proto].keys()

            for port in ports:
                service = nm[host][proto][port]['name']

                services.append({
                    "port": port,
                    "service": service
                })

    return services