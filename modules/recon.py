import socket
from modules.report import save_report

def recon_module():
    target = input("Enter domain or IP: ")
    target = target.replace("http://","").replace("https://","").split("/")[0]

    report = f"Recon Report\nTarget: {target}\n\n"

    try:
        ip = socket.gethostbyname(target)
        print(f"[+] IP: {ip}")
        report += f"IP: {ip}\n"
    except:
        print("[-] Failed")
        return

    save_report("recon", report)
