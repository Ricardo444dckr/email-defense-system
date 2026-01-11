import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env (se existir)
load_dotenv()

# Diretório base do projeto
basedir = os.path.abspath(os.path.dirname(__file__))

# Caminho da pasta de relatórios
reports_dir = os.path.join(basedir, "reports")
os.makedirs(reports_dir, exist_ok=True)  # cria a pasta se não existir

class Config:
    """Configurações centrais da aplicação Flask."""
    SECRET_KEY = os.getenv("SECRET_KEY", "default-key")

    # Tenta ler DATABASE_URL da nuvem; senão, usa SQLite local
    SQLALCHEMY_DATABASE_URI = (
        os.getenv("DATABASE_URL")
        or "sqlite:///" + os.path.join(reports_dir, "report.db")
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False