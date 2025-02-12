from flask import request
from flask_restx import Namespace, Resource
from app.main.service.tipo_service import get_tipo_by_id
from app.main.utils.schema import basic_schema, tipo_schema

# 🔹 Criando apenas o Namespace (o Blueprint será registrado no app/__init__.py)
api = Namespace("tipo", description="Operações relacionadas a Tipos")

@api.route("")
class Tipo(Resource):
    @api.response(200, "Success")
    @api.param("id", "Id do tipo")
    @api.marshal_with(tipo_schema)
    def get(self):
        id_tipo = request.args.get("id")
        if not id_tipo:
            return {"error": "ID do tipo é obrigatório"}, 400
        
        tipo = get_tipo_by_id(id_tipo)
        if not tipo:
            return {"error": "Tipo não encontrado"}, 404
        
        return tipo
