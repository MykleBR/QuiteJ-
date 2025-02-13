from app.main.model.tipo import Tipo
from app.main import db

def get_tipo_by_id(id_tipo):
    return Tipo.query.get(id_tipo)