import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from modules.report import save_report
from modules.utils import progress_bar

# =========================
# 🧠 AI-LIKE DETECTION
# =========================
def ai_detect(text):
    findings = []
    t = text.lower()

    if "sql" in t and "error" in t:
        findings.append("Possible SQL Injection")

    if "<script>" in t:
        findings.append("Possible XSS")

    if "unauthorized" in t or "forbidden" in t:
        findings.append("Access Control Issue")

    return findings


# =========================
# 🌐 CRAWLER
# =========================
def crawl(url):
    links = set()

    try:
        r = requests.get(url, timeout=5)
        soup = BeautifulSoup(r.text, "html.parser")

        for a in soup.find_all("a", href=True):
            link = urljoin(url, a["href"])
            if url in link:
                links.add(link)

    except:
        pass

    return list(links)


# =========================
# 🧾 FORM EXTRACTOR
# =========================
def get_forms(url):
    try:
        r = requests.get(url, timeout=5)
        soup = BeautifulSoup(r.text, "html.parser")
        return soup.find_all("form")
    except:
        return []


# =========================
# 💉 TEST FORM
# =========================
def test_form(form, url):
    results = []

    action = form.get("action")
    method = form.get("method", "get").lower()

    post_url = urljoin(url, action)
    inputs = form.find_all("input")

    data = {}

    for i in inputs:
        name = i.get("name")
        if name:
            data[name] = "test"

    # XSS Payload
    xss_payload = "<script>alert(1)</script>"
    for key in data:
        data[key] = xss_payload

    try:
        if method == "post":
            res = requests.post(post_url, data=data)
        else:
            res = requests.get(post_url, params=data)

        if xss_payload in res.text:
            results.append(f"[VULN] XSS in form: {post_url}")

    except:
        pass

    return results


# =========================
# 💣 SQLi TEST
# =========================
def test_sqli(url):
    payload = "' OR '1'='1"
    try:
        r = requests.get(url + "?id=" + payload)
        if "sql" in r.text.lower() or "error" in r.text.lower():
            return "[VULN] Possible SQL Injection"
    except:
        pass
    return None


# =========================
# 🌍 MAIN SCANNER
# =========================
def web_scanner():
    url = input("Enter URL: ")

    print("\n[+] Starting Advanced Web Scan...\n")

    report = f"Advanced Web Scan Report\nTarget: {url}\n\n"

    progress_bar(40, "Scanning")

    # =========================
    # 🌐 CRAWL
    # =========================
    print("[+] Crawling links...")
    links = crawl(url)

    for link in links:
        print(f"[LINK] {link}")
        report += f"Link: {link}\n"

    # =========================
    # 🧾 FORMS
    # =========================
    print("\n[+] Detecting forms...")
    forms = get_forms(url)

    report += f"\nForms found: {len(forms)}\n"

    for form in forms:
        print("[FORM] Found form")

    # =========================
    # 💉 FORM TEST
    # =========================
    print("\n[+] Testing forms for XSS...")
    for form in forms:
        results = test_form(form, url)
        for r in results:
            print(r)
            report += r + "\n"

    # =========================
    # 💣 SQLi
    # =========================
    print("\n[+] Testing SQL Injection...")
    sqli = test_sqli(url)
    if sqli:
        print(sqli)
        report += sqli + "\n"

    # =========================
    # 🔐 HEADERS
    # =========================
    print("\n[+] Checking headers...")
    try:
        r = requests.get(url)
        if "Content-Security-Policy" not in r.headers:
            print("[WARN] Missing CSP")
            report += "Missing CSP\n"
    except:
        pass

    # =========================
    # 🧠 AI ANALYSIS
    # =========================
    print("\n[+] AI Analysis...")
    findings = ai_detect(r.text)

    for f in findings:
        print(f"[AI] {f}")
        report += f + "\n"

    # =========================
    # 🧾 SAVE REPORT
    # =========================
    save_report("webscan_advanced", report)

    print("\n[✓] Scan Complete\n")
