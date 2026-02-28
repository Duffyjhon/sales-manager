from backend.models.venda import Venda
from backend.extensions import db
from datetime import datetime


class VendaService:

    @staticmethod
    def listar_vendas():
        return Venda.query.all()

    @staticmethod
    def criar_venda(cliente, produto, valor):
        nova = Venda(
            cliente=cliente,
            produto=produto,
            valor=valor,
            data_venda=datetime.now()
        )
        db.session.add(nova)
        db.session.commit()
        return nova

    @staticmethod
    def deletar_venda(venda_id):
        venda = Venda.query.get(venda_id)

        if not venda:
            return False

        db.session.delete(venda)
        db.session.commit()
        return True