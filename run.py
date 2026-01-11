import os
from app import create_app

# Cria a instância principal da aplicação Flask
app = create_app()

# ---------------------------------------------------------------
# 1️⃣  Rota inicial (exibe status do servidor)
# ---------------------------------------------------------------
@app.route("/")
def home():
    return (
        "<h2>✅ Servidor Email‑Defense ativo!</h2>"
        "<p>Use o endpoint <b>/analyze</b> com método POST "
        "para analisar e‑mails.</p>"
    )

# ---------------------------------------------------------------
# 2️⃣  Execução da aplicação
# ---------------------------------------------------------------
if __name__ == "__main__":
    # A plataforma Render define a porta na variável de ambiente PORT
    port = int(os.environ.get("PORT", 5000))
    # O host 0.0.0.0 permite acesso externo (necessário no Render)
    app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)