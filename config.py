import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente (.env)
load_dotenv()

# Diretório base do projeto
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Caminho do arquivo SQLite — vai para /tmp, que é gravável no Render
DB_PATH = "/tmp/report.db"

class Config:
    """Configuração central da aplicação Flask."""
    SECRET_KEY = os.getenv("SECRET_KEY", "default-key")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL") or f"sqlite:///{DB_PATH}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False