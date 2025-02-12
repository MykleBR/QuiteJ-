from app.main import db, create_app
from app.main.model.tipo import Tipo
import pandas as pd

app = create_app()

with app.app_context():
    db.create_all()
    tipos_csv = "tipos.csv"
    df_tipos = pd.read_csv(tipos_csv)
    
    for _, row in df_tipos.iterrows():
        tipo = Tipo(id=row["id"], nome=row["nome"])
        db.session.add(tipo)
    
    db.session.commit()
    print("Banco de dados populado com sucesso!")