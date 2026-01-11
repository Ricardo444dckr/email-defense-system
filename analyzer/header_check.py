def analyze_headers(headers):
    reasons = []
    score = 0

    if "spf=fail" in headers.lower():
        reasons.append("Falha na verificação SPF")
        score += 2

    if "dkim=fail" in headers.lower():
        reasons.append("Falha na verificação DKIM")
        score += 2

    return score, reasons
import re

def analyze_headers(headers: str):
    """Analisa cabeçalhos de email para detetar falhas de autenticação e anomalias."""
    reasons = []
    score = 0
    headers_lower = headers.lower()

    # SPF (Sender Policy Framework)
    if "spf=pass" in headers_lower:
        reasons.append("SPF passou ✅")
    elif "spf=fail" in headers_lower:
        reasons.append("Falha na verificação SPF ❌")
        score += 2
    elif "spf=softfail" in headers_lower:
        reasons.append("SPF softfail ⚠️")
        score += 1
    else:
        reasons.append("SPF não encontrado ⚠️")
        score += 1

    # DKIM (DomainKeys Identified Mail)
    if "dkim=pass" in headers_lower:
        reasons.append("DKIM passou ✅")
    elif "dkim=fail" in headers_lower:
        reasons.append("Falha na verificação DKIM ❌")
        score += 2
    else:
        reasons.append("DKIM ausente ⚠️")
        score += 1

    # DMARC
    if "dmarc=pass" in headers_lower:
        reasons.append("DMARC passou ✅")
    elif "dmarc=fail" in headers_lower:
        reasons.append("Falha na verificação DMARC ❌")
        score += 2
    else:
        reasons.append("DMARC não encontrado ⚠️")
        score += 1

    # Received chain
    hops = len(re.findall(r"received:", headers_lower))
    if hops > 7:
        reasons.append(f"Cabeçalho com {hops} hops — possível encaminhamento excessivo ⚠️")
        score += 1

    # From / Return-Path desalinhados
    from_match = re.search(r"from:\s*(.*)", headers_lower)
    return_path_match = re.search(r"return-path:\s*(.*)", headers_lower)
    if from_match and return_path_match:
        if return_path_match.group(1).strip() not in from_match.group(1):
            reasons.append("From e Return‑Path diferentes (possível spoofing) ❌")
            score += 2

    return score, reasons