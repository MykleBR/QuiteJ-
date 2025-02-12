from flask import Blueprint
from flask_restx import Api
from app.main.api.routes import api as tipo_ns

blueprint = Blueprint("api", __name__, url_prefix="/api")

api = Api(
    blueprint,
    version="1.0",
    title="API - QuiteJá",
    description="API",
)

api.add_namespace(tipo_ns, "/tipo")
