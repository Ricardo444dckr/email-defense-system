import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente (se existir .env)
load_dotenv()

# Caminho base do projeto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Caminho absoluto para o arquivo da base de dados
db_path = os.path.join(BASE_DIR, "report.db")

# Cria o arquivo vazio se não existir (para evitar erro do Render)
if not os.path.exists(db_path):
    open(db_path, "a").close()


class Config:
    """Configuração Global do Flask"""

    SECRET_KEY = os.getenv("SECRET_KEY", "default-key")

    # Se o Render tiver uma DATABASE_URL (Postgres), usa-a;
    # senão, usa o SQLite criado acima.
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL") or f"sqlite:///{db_path}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False