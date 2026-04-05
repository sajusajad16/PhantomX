from datetime import datetime
import os

if not os.path.exists("reports"):
    os.makedirs("reports")

def save_report(name, content):
    filename = f"reports/{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w") as f:
        f.write(content)
    print(f"[+] Report saved: {filename}")
