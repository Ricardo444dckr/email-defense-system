from flask import Flask, request, jsonify
from flask_cors import CORS
from analyzer.text_check import analyze_text
from analyzer.link_check import analyze_links
from analyzer.header_check import analyze_headers
import os

# Cria a aplicação Flask
app = Flask(__name__)

# Autoriza chamadas de qualquer origem (ex: Gmail, navegador, extensão)
CORS(
    app,
    supports_credentials=True,
    methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type"],
    resources={r"/*": {"origins": "*"}}
)

# ---------------------------------------------------------------
# 1️⃣  Rota inicial: mensagem quando alguém abre o domínio raiz
# ---------------------------------------------------------------
@app.route("/")
def home():
    return (
        "<h2>✅ Servidor Email‑Defense ativo!</h2>"
        "<p>Use o endpoint <b>/analyze</b> com método POST "
        "para analisar e‑mails.</p>"
    )

# ---------------------------------------------------------------
# 2️⃣  Rota principal: análise de e‑mails maliciosos
# ---------------------------------------------------------------
@app.route("/analyze", methods=["POST"])
def analyze_email():
    data = request.json or {}
    text = data.get("body", "")
    headers = data.get("headers", "")

    score = 0
    reasons = []

    # Texto
    s, r = analyze_text(text)
    score += s
    reasons.extend(r)

    # Links
    s, r = analyze_links(text)
    score += s
    reasons.extend(r)

    # Headers
    s, r = analyze_headers(headers)
    score += s
    reasons.extend(r)

    # Decisão final
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
# 3️⃣  Execução do servidor
# ---------------------------------------------------------------
if __name__ == "__main__":
    # No Render, a porta vem da variável de ambiente PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)