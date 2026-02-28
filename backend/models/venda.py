from backend.extensions import db
from datetime import datetime

class Venda(db.Model):
    __tablename__ = "vendas"

    id = db.Column(db.Integer, primary_key=True)
    cliente = db.Column(db.String(120), nullable=False)
    produto = db.Column(db.String(120), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    data_venda = db.Column(db.DateTime, default=datetime.utcnow)