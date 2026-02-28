from flask import Blueprint, request, jsonify
from backend.services.auth_service import AuthService

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


@auth_bp.post("/register")
def registrar():
    dados = request.json
    username = dados.get("username")
    password = dados.get("password")

    user, error = AuthService.registrar(username, password)

    if error:
        return jsonify({"error": error}), 400

    return jsonify({"message": "Usuário registrado com sucesso", "username": user.username})


@auth_bp.post("/login")
def login():
    dados = request.json
    username = dados.get("username")
    password = dados.get("password")

    token, error = AuthService.login(username, password)

    if error:
        return jsonify({"error": error}), 400

    return jsonify({"token": token})
