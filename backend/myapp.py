from flask import Flask, send_from_directory
from backend.extensions import db, migrate, jwt, bcrypt
from backend.config import Config
from backend.routes.auth_routes import auth_bp
from backend.routes.venda_routes import vendas_bp
from backend.routes.dashboard_routes import dashboard_bp
from backend.routes.export_routes import export_bp

def create_app():
    app = Flask(
        __name__,
        static_folder="../frontend",
        static_url_path=""
    )

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    bcrypt.init_app(app)

    # Blueprints
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(vendas_bp, url_prefix="/vendas")
    app.register_blueprint(dashboard_bp, url_prefix="/dashboard")
    app.register_blueprint(export_bp, url_prefix="/vendas/export")
    @app.route("/")
    def home():
        return send_from_directory(app.static_folder, "login.html")

    return app
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="127.0.0.1", port=5000)
