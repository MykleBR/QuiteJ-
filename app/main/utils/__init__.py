# app/main/utils/__init__.py
import os
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.main.config import config_by_name

app = Flask(__name__)
app.config.from_object(config_by_name[os.getenv("FLASK_ENV", "default")])

db = SQLAlchemy(app, session_options={"autoflush": False})
migrate = Migrate(app, db)
