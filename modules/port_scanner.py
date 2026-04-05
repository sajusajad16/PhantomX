import socket
from modules.report import save_report
from modules.utils import progress_bar

def port_scanner():
    target = input("Enter target IP: ")
    report = f"Port Scan Report\nTarget: {target}\n\nOpen Ports:\n"

    ports = [21, 22, 80, 443]

    progress_bar(len(ports), "Scanning Ports")

    for port in ports:
        s = socket.socket()
        s.settimeout(1)

        if s.connect_ex((target, port)) == 0:
            print(f"[OPEN] Port {port}")
            report += f"- Port {port}\n"

        s.close()

    save_report("portscan", report)
