from flask import Flask, request, jsonify
from flask_cors import CORS                   # ← 1. importa o CORS
from analyzer.text_check import analyze_text
from analyzer.link_check import analyze_links
from analyzer.header_check import analyze_headers

app = Flask(__name__)
# ← 2. autoriza chamadas de qualquer origem (como o Gmail)
CORS(app, supports_credentials=True,
     methods=["GET", "POST", "OPTIONS"],
     allow_headers=["Content-Type"],
     resources={r"/*": {"origins": "*"}})

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

# ← 3. garante que o Flask não recria sessões e não abre novas janelas
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)