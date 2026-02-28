from backend.models.user import User
from backend.extensions import db, bcrypt
from flask_jwt_extended import create_access_token
from datetime import timedelta


class AuthService:

    @staticmethod
    def registrar(username: str, password: str):
        if User.query.filter_by(username=username).first():
            return None, "Usuário já existe"

        user = User(username=username)
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        return user, None

    @staticmethod
    def login(username: str, password: str):
        user = User.query.filter_by(username=username).first()

        if not user:
            return None, "Usuário não encontrado"

        if not user.check_password(password):
            return None, "Senha incorreta"

        token = create_access_token(identity=user.id, expires_delta=timedelta(hours=8))
        return token, None
