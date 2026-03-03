from collections import defaultdict
from backend.models.venda import Venda


class DashboardService:

    @staticmethod
    def gerar_dashboard():
        vendas = Venda.query.all()

        total_vendas = len(vendas)
        valor_total = sum((v.valor or 0) for v in vendas)
        valor_medio = (valor_total / total_vendas) if total_vendas else 0

        # 🔹 Vendas por produto (mantém)
        vendas_por_produto = {}
        for v in vendas:
            nome_produto = (v.produto or "Sem produto").strip()
            vendas_por_produto[nome_produto] = vendas_por_produto.get(nome_produto, 0) + (v.valor or 0)

        # 🔹 NOVO: Vendas por mês
        vendas_por_mes = defaultdict(float)

        for v in vendas:
            if not v.data_venda:
                continue

            mes = v.data_venda.strftime("%Y-%m")
            vendas_por_mes[mes] += (v.valor or 0)

        vendas_por_mes_ordenado = dict(sorted(vendas_por_mes.items()))

        return {
            "total_vendas": total_vendas,
            "total_valor": float(valor_total),
            "media_valor": float(valor_medio),
            "vendas_por_produto": vendas_por_produto,
            "vendas_por_mes": vendas_por_mes_ordenado
        }