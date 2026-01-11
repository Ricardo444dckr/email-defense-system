from flask import Blueprint, request, jsonify
from analyzer.text_check import analyze_text
from analyzer.link_check import analyze_links
from analyzer.header_check import analyze_headers
from app import db
from app.models import Analysis

main = Blueprint("main", __name__)

@main.route("/analyze", methods=["POST"])
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

    # Grava no banco de dados
    new_record = Analysis(
        sender=headers,
        verdict=verdict,
        score=score
    )
    db.session.add(new_record)
    db.session.commit()

    # Retorna resultado à extensão
    return jsonify({
        "veredito": verdict,
        "score": score,
        "motivos": reasons
    })