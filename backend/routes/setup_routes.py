from flask import Blueprint, jsonify
from backend.extensions import db, bcrypt
from backend.models.user import User

setup_bp = Blueprint("setup", __name__, url_prefix="/setup")


@setup_bp.get("/create-admin")
def create_admin():

    if User.query.filter_by(username="admin").first():
        return jsonify({"message": "Admin já existe"})

    senha_hash = bcrypt.generate_password_hash("123456").decode("utf-8")

    admin = User(
        username="admin",
        password_hash=senha_hash
    )

    db.session.add(admin)
    db.session.commit()

    return jsonify({
        "message": "Admin criado com sucesso",
        "username": "admin",
        "password": "123456"
    })