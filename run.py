import os
from app import create_app, db  # importa a instância db que já existe no pacote app

# ---------------------------------------------------------------
# 1️⃣  Cria a instância principal da aplicação Flask
# ---------------------------------------------------------------
app = create_app()

# ---------------------------------------------------------------
# 2️⃣  Garante que o banco e suas tabelas existam
# ---------------------------------------------------------------
with app.app_context():
    db.create_all()

# ---------------------------------------------------------------
# 3️⃣  Executa o servidor (Render e Local)
# ---------------------------------------------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)