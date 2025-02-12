# app/main/config.py
import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "my_precious_secret_key")
    FLASK_PORT = os.getenv("PORT", 5000)
    FLASK_HOST = os.getenv("HOST", "0.0.0.0")
    DEBUG = False
    RESTX_MASK_SWAGGER = False

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://postgres:admin@localhost:5432/postgres")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False

config_by_name = dict(
    DEV=DevelopmentConfig,
    default=DevelopmentConfig
)
