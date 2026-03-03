from backend.models.venda import Venda
from backend.extensions import db
from datetime import datetime


class VendaService:

    @staticmethod
    def listar_vendas():
        return Venda.query.all()

    @staticmethod
    def criar_venda(cliente, produto, valor, data_venda=None):
        """
        data_venda pode ser:
          - None (usa data/hora atual)
          - string "YYYY-MM-DD" (vinda do front)
          - datetime (se você quiser passar já convertido)
        """
        kwargs = {
            "cliente": cliente,
            "produto": produto,
            "valor": valor,
        }

        if isinstance(data_venda, str) and data_venda.strip():
            try:
                # Recebe "YYYY-MM-DD" do input type="date"
                kwargs["data_venda"] = datetime.strptime(data_venda, "%Y-%m-%d")
            except ValueError:
                raise ValueError("data_venda inválida. Use YYYY-MM-DD.")
        elif isinstance(data_venda, datetime):
            kwargs["data_venda"] = data_venda
        else:
            # Se não veio data, usa agora (padrão consistente com Render)
            kwargs["data_venda"] = datetime.utcnow()

        nova = Venda(**kwargs)
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