from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.main.config import config_by_name
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config_by_name[os.getenv("FLASK_ENV", "default")])
    db.init_app(app)

    with app.app_context():
        from app import blueprint
        app.register_blueprint(blueprint)
        db.create_all()

    return app
