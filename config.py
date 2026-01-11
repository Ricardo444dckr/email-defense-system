import os
from dotenv import load_dotenv

# ---------------------------------------------------------------
# 1️⃣  Carrega variáveis de ambiente (.env) se existirem
# ---------------------------------------------------------------
load_dotenv()

# Diretório base do projeto
basedir = os.path.abspath(os.path.dirname(__file__))

# Caminho absoluto da pasta 'reports'
reports_dir = os.path.join(basedir, "reports")

# Garante que a pasta exista (necessário no Render)
os.makedirs(reports_dir, exist_ok=True)

# ---------------------------------------------------------------
# 2️⃣  Classe de configuração principal
# ---------------------------------------------------------------
class Config:
    """Configurações centrais da aplicação Flask."""

    # Chave secreta da aplicação
    SECRET_KEY = os.getenv("SECRET_KEY", "default-key")

    # URL do banco de dados:
    # - se houver DATABASE_URL (ex: PostgreSQL no Render), usa ela;
    # - senão, cria e usa um SQLite local dentro da pasta 'reports'.
    SQLALCHEMY_DATABASE_URI = (
        os.getenv("DATABASE_URL")
        or "sqlite:///" + os.path.join(reports_dir, "report.db")
    )

    # Desativa rastreamento 