from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flasgger import Swagger
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
jwt = JWTManager()
swagger = Swagger()
migrate = Migrate()
bcrypt = Bcrypt()
