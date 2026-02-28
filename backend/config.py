import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "development-secret-key")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "dev-jwt-key")

    # Prioriza Postgres (Render) se existir DATABASE_URL
    _db_url = os.getenv("DATABASE_URL")

    if _db_url:
        # Alguns providers usam postgres://, mas o SQLAlchemy prefere postgresql://
        if _db_url.startswith("postgres://"):
            _db_url = _db_url.replace("postgres://", "postgresql://", 1)
        SQLALCHEMY_DATABASE_URI = _db_url
    else:
        # Local: cai para SQLite
        SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER = {"title": "API de Vendas", "uiversion": 3}