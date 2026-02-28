from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from backend.models.user import User

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.post("/login")
def login():
    data = request.get_json(silent=True) or {}
    username = (data.get("username") or "").strip()
    password = data.get("password") or ""

    if not username or not password:
        return jsonify({"error": "Informe usuário e senha"}), 400

    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return jsonify({"error": "Usuário ou senha incorretos"}), 401

    token = create_access_token(identity={"id": user.id, "username": user.username})
    return jsonify({"token": token}), 200