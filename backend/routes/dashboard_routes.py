from flask import Blueprint, jsonify
from backend.services.dashboard_service import DashboardService

dashboard_bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")


@dashboard_bp.get("/")
def get_dashboard():
    dados = DashboardService.gerar_dashboard()
    return jsonify(dados)
