from scanner import scan_target
from analyzer import analyze_services
from report import generate_report

target = input("Enter target IP or domain: ")

services = scan_target(target)

vulnerabilities = analyze_services(services)

generate_report(target, services, vulnerabilities)