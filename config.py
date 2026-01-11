import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente (.env)
load_dotenv()

class Config:
    """Configuração simplificada para o Render"""
    SECRET_KEY = os.getenv("SECRET_KEY", "default-key")

    # Usa banco de dados temporário em memória (evita erro de permissão com SQLite)
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"

    SQLALCHEMY_TRACK_MODIFICATIONS = False