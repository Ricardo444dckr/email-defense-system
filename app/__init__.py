from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app, supports_credentials=True)
    db.init_app(app)

    # importe e registre o blueprint dentro da função
    from app.routes.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app