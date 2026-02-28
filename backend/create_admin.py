from backend.myapp import create_app
from backend.extensions import db, bcrypt
from backend.models.user import User

app = create_app()

with app.app_context():
    username = "admin"
    senha = "123456"

    existe = User.query.filter_by(username=username).first()

    if existe:
        print("⚠️ Usuário admin já existe.")
    else:
        senha_hash = bcrypt.generate_password_hash(senha).decode("utf-8")

        admin = User(
            username=username,
            password_hash=senha_hash   # ⭐ nome mais comum
        )

        db.session.add(admin)
        db.session.commit()

        print("✅ Usuário admin criado com sucesso!")
        print("👤 Usuário: admin")
        print("🔒 Senha: 123456")