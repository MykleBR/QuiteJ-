# app/main/utils/schema.py
import json
from flask_restx import fields
from flask_restx.model import Model

# 🔹 Custom Fields
class JSONField(fields.Raw):
    def format(self, value):
        return json.loads(value)
    
class NullableString(fields.String):
    __schema_type__ = ["string", "null"]

class NullableInteger(fields.Integer):
    __schema_type__ = ["integer", "null"]

class NullableFloat(fields.Float):
    __schema_type__ = ["float", "null"]

# 🔹 Definição dos Modelos RESTx
basic_schema = Model(
    "Basic",
    {
        "id": fields.String(readonly=True),
        "name": fields.String(readonly=True),
    },
)

tipo_schema = Model(
    "Tipo",
    {
        "id": fields.Integer(),
        "nome": fields.String(),
    },
)
