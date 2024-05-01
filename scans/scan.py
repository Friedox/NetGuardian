# scans/scan.py

import nmap


async def perform_scan():
    # Perform network scan using Nmap
    nm = nmap.PortScanner()
    scan_result = nm.scan(hosts='127.0.0.1', arguments='-F')

    # Extract and format scan results
    output = "Scan Results:\n"
    for host in nm.all_hosts():
        output += f"Host: {host}\n"
        for proto in nm[host].all_protocols():
            output += f"Protocol: {proto}\n"
            ports = nm[host][proto].keys()
            for port in ports:
                output += f"Port: {port} - {nm[host][proto][port]['state']}\n"

    return output
