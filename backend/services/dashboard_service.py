from backend.models.venda import Venda


class DashboardService:

    @staticmethod
    def gerar_dashboard():
        vendas = Venda.query.all()

        total_vendas = len(vendas)
        valor_total = sum(v.valor for v in vendas)
        valor_medio = valor_total / total_vendas if total_vendas else 0

        vendas_por_produto = {}
        for v in vendas:
            vendas_por_produto[v.produto] = vendas_por_produto.get(v.produto, 0) + v.valor

        return {
            "total_vendas": total_vendas,
            "total_valor": valor_total,
            "media_valor": valor_medio,
            "vendas_por_produto": vendas_por_produto
        }
