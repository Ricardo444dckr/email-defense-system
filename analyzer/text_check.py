SUSPICIOUS_KEYWORDS = [
    "urgente",
    "clique aqui",
    "verifique sua conta",
    "senha",
    "pagamento pendente",
    "conta bloqueada"
]

def analyze_text(text):
    score = 0
    reasons = []

    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword.lower() in text.lower():
            score += 1
            reasons.append(f"Palavra suspeita detectada: '{keyword}'")

    return score, reasons