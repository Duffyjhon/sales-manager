import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "development-secret-key")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "dev-jwt-key")
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SWAGGER = {
        "title": "API de Vendas",
        "uiversion": 3
    }
