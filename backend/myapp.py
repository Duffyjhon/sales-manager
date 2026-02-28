from flask import Flask, send_from_directory
import os

from backend.extensions import db, migrate, jwt, bcrypt
from backend.config import Config

from backend.routes.setup_routes import setup_bp
from backend.routes.venda_routes import vendas_bp
from backend.routes.dashboard_routes import dashboard_bp
from backend.routes.export_routes import export_bp
from backend.routes.auth_login_routes import auth_bp

def create_app():
    app = Flask(
        __name__,
        static_folder="../frontend",
        static_url_path=""
    )

    # Carrega configurações gerais (SECRET_KEY, JWT, etc.)
    app.config.from_object(Config)

    # ✅ Garante que a pasta instance exista no Render e local
    os.makedirs(app.instance_path, exist_ok=True)

    # ✅ Força o SQLite a usar caminho absoluto (evita erro no Render)
    db_path = os.path.join(app.instance_path, "database.db")
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Extensões
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    bcrypt.init_app(app)

    # ✅ Garante tabelas no deploy (evita 500 por "no such table")
    # Para produção "de empresa", depois trocamos para migrations + Postgres.
    with app.app_context():
        db.create_all()

    # Blueprints (sem duplicar prefixos)

    app.register_blueprint(vendas_bp)     # vendas_bp já tem url_prefix="/vendas"
    app.register_blueprint(dashboard_bp)  # dashboard_bp já tem url_prefix="/dashboard"
    app.register_blueprint(export_bp)     # export_bp já tem url_prefix="/vendas/export"
    app.register_blueprint(setup_bp)
    app.register_blueprint(auth_bp)
    # Home -> login.html
    @app.route("/")
    def home():
        return send_from_directory(app.static_folder, "login.html")

    return app


if __name__ == "__main__":
    app = create_app()
    # Local: host 127.0.0.1
    app.run(debug=True, host="127.0.0.1", port=5000)