# app/main/model/tipo.py
from app.main import db

class Tipo(db.Model):
    __tablename__ = "tipos"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)