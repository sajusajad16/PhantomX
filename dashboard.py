from flask import Flask, render_template, request
import os
from modules.port_scanner import port_scanner
from modules.web_scanner import web_scanner

app = Flask(__name__)

output_data = ""

@app.route("/", methods=["GET", "POST"])
def home():
    global output_data

    if request.method == "POST":
        target = request.form.get("target")
        scan_type = request.form.get("scan")

        output_data = f"[+] Running {scan_type} on {target}\n"

        if scan_type == "port":
            output_data += "Port scan started...\n"
        elif scan_type == "web":
            output_data += "Web scan started...\n"

    reports = os.listdir("reports")

    return render_template("index.html", reports=reports, output=output_data)


if __name__ == "__main__":
    app.run(debug=True)
