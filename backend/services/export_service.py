from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from openpyxl import Workbook
from backend.models.venda import Venda


class ExportService:
    @staticmethod
    def exportar_excel_bytes():
        vendas = Venda.query.all()

        wb = Workbook()
        ws = wb.active
        ws.title = "Vendas"

        ws.append(["ID", "Cliente", "Produto", "Valor", "Data"])

        for v in vendas:
            data_txt = v.data_venda.strftime("%d/%m/%Y %H:%M") if getattr(v, "data_venda", None) else ""
            ws.append([v.id, v.cliente, v.produto, float(v.valor), data_txt])

        output = BytesIO()
        wb.save(output)
        output.seek(0)
        return output

    @staticmethod
    def exportar_pdf_bytes():
        vendas = Venda.query.all()

        output = BytesIO()
        c = canvas.Canvas(output, pagesize=letter)

        # Fonte com suporte a acentos (se você tiver o arquivo .ttf no projeto)
        # Coloque o arquivo: backend/assets/fonts/DejaVuSans.ttf
        font_name = "Helvetica"
        try:
            pdfmetrics.registerFont(TTFont("DejaVuSans", "backend/assets/fonts/DejaVuSans.ttf"))
            font_name = "DejaVuSans"
        except Exception:
            # Se não existir a fonte, usa Helvetica mesmo (mas pode não renderizar alguns acentos)
            font_name = "Helvetica"

        c.setFont(font_name, 16)
        c.drawString(180, 760, "Relatório de Vendas")

        y = 720
        c.setFont(font_name, 11)

        def safe_text(s: str) -> str:
            # Evita caracteres que podem quebrar com Helvetica (quando não houver TTF)
            if font_name != "Helvetica":
                return s
            return s.encode("latin-1", "replace").decode("latin-1")

        for v in vendas:
            data_txt = v.data_venda.strftime("%d/%m/%Y") if getattr(v, "data_venda", None) else ""
            linha = f"{v.id} | {v.cliente} | {v.produto} | R$ {float(v.valor):.2f} | {data_txt}"

            linha = safe_text(linha)

            # quebra de página
            if y < 60:
                c.showPage()
                c.setFont(font_name, 11)
                y = 720

            c.drawString(40, y, linha)
            y -= 18

        c.showPage()
        c.save()

        output.seek(0)
        return output