import os
from app import create_app

# Cria a instância da aplicação Flask
app = create_app()

if __name__ == "__main__":
    # O Render fornece a porta automaticamente pela variável de ambiente PORT
    port = int(os.environ.get("PORT", 5000))
    # host="0.0.0.0" → permite conexões externas (necessário para servidor online)
    app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)