import os
from app import create_app
from flask_sqlalchemy import SQLAlchemy

# ---------------------------------------------------------------
# 1️⃣  Cria a instância principal da aplicação Flask
# ---------------------------------------------------------------
app = create_app()

# ---------------------------------------------------------------
# 2️⃣  Inicializa o SQLAlchemy e garante a criação das tabelas
# ---------------------------------------------------------------
db = SQLAlchemy(app)
with app.app_context():
    db.create_all()

# ---------------------------------------------------------------
# 3️⃣  Execução do servidor (Render e local)
# ---------------------------------------------------------------
if __name__ == "__main__":
    # O Render fornece a porta automaticamente pela variável de ambiente PORT
    port = int(os.environ.get("PORT", 5000))
    # host="0.0.0.0" permite conexões externas (necessário para o Render)
    app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)