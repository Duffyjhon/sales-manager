from flask import Blueprint, send_file
from datetime import datetime

from backend.services.export_service import ExportService

export_bp = Blueprint("export", __name__, url_prefix="/vendas/export")


@export_bp.get("/excel")
def exportar_excel():
    arquivo = ExportService.exportar_excel_bytes()
    nome = f"vendas_{datetime.now().strftime('%Y-%m-%d')}.xlsx"

    return send_file(
        arquivo,
        as_attachment=True,
        download_name=nome,
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )


@export_bp.get("/pdf")
def exportar_pdf():
    arquivo = ExportService.exportar_pdf_bytes()
    nome = f"vendas_{datetime.now().strftime('%Y-%m-%d')}.pdf"

    return send_file(
        arquivo,
        as_attachment=True,
        download_name=nome,
        mimetype="application/pdf"
    )