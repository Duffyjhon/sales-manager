from collections import defaultdict
from backend.models.venda import Venda
from datetime import datetime

class DashboardService:

    @staticmethod
    def gerar_dashboard():
        vendas = Venda.query.all()

        total_vendas = len(vendas)
        valor_total = sum(v.valor for v in vendas)
        valor_medio = valor_total / total_vendas if total_vendas else 0

        vendas_por_mes = defaultdict(float)

        for v in vendas:
            mes = v.data_venda.strftime("%Y-%m")
            vendas_por_mes[mes] += v.valor

        vendas_por_mes = dict(sorted(vendas_por_mes.items()))

        # Crescimento percentual
        meses = list(vendas_por_mes.values())
        crescimento = 0

        if len(meses) >= 2 and meses[-2] != 0:
            crescimento = ((meses[-1] - meses[-2]) / meses[-2]) * 100

        # Melhor mês
        melhor_mes = None
        if vendas_por_mes:
            melhor_mes = max(vendas_por_mes, key=vendas_por_mes.get)

        return {
            "total_vendas": total_vendas,
            "total_valor": valor_total,
            "media_valor": valor_medio,
            "vendas_por_mes": vendas_por_mes,
            "crescimento_percentual": round(crescimento, 2),
            "melhor_mes": melhor_mes
        }