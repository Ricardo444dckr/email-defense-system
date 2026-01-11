from flask import Flask, request, jsonify
from flask_cors import CORS
from analyzer.text_check import analyze_text
from analyzer.link_check import analyze_links
from analyzer.header_check import analyze_headers
import os

# ---------------------------------------------------------------
# 1️⃣  Criação e configuração base da aplicação Flask
# ---------------------------------------------------------------
app = Flask(__name__)

# Autorização de chamadas de qualquer origem (Gmail, navegador, extensão)
# '*' aceita tudo; se desejar restringir, define origens específicas.
CORS(
    app,
    origins="*",
    supports_credentials=True,
    methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type"]
)

# ---------------------------------------------------------------
# 2️⃣  Rota inicial (exibe status do servidor)
# ---------------------------------------------------------------
@app.route("/")
def home():
    return (
        "<h2>✅ Servidor Email‑Defense ativo!</h2>"
        "<p>Use o endpoint <b>/analyze</b> com método POST "
        "para analisar e‑mails.</p>"
    )

# ---------------------------------------------------------------
# 3️⃣  Endpoint principal de análise de e‑mail
# ---------------------------------------------------------------
@app.route("/analyze", methods=["POST"])
def analyze_email():
    data = request.json or {}
    text = data.get("body", "")
    headers = data.get("headers", "")

    score = 0
    reasons = []

    # 3.1  Verifica palavras suspeitas
    s, r = analyze_text(text)
    score += s
    reasons.extend(r)

    # 3.2  Verifica links
    s, r = analyze_links(text)
    score += s
    reasons.extend(r)

    # 3.3  Verifica cabeçalhos
    s, r = analyze_headers(headers)
    score += s
    reasons.extend(r)

    # 3.4  Define o veredito
    if score >= 5:
        verdict = "Malicioso"
    elif score >= 3:
        verdict = "Suspeito"
    else:
        verdict = "Seguro"

    return jsonify({
        "veredito": verdict,
        "score": score,
        "motivos": reasons
    })

# ---------------------------------------------------------------
# 4️⃣  Execução da aplicação
# ---------------------------------------------------------------
if __name__ 