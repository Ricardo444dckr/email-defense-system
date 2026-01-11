import re
from analyzer.virus_total import check_url

URL_REGEX = r'(https?://[^\s]+)'

def analyze_links(text):
    links = re.findall(URL_REGEX, text)
    reasons = []
    score = 0

    for link in links:
        # Regras locais
        if "bit.ly" in link or "tinyurl" in link:
            reasons.append("Uso de encurtador de URL")
            score += 1
        if link.count('.') > 4:
            reasons.append("URL excessivamente longa/suspeita")
            score += 1

        # ---- Verificação VirusTotal ----
        vt_mal, vt_reason = check_url(link)
        if vt_mal:
            reasons.append(vt_reason)
            score += 2

    return score, reasons