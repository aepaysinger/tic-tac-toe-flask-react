import os

from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from flask_cors import CORS
from flask_migrate import Migrate
from db import db
from flask import Flask
# from main_bp import main as main_blueprint
from auth import auth as auth_blueprint
from flask_login import LoginManager
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, unset_jwt_cookies, jwt_required, JWTManager
from models import User



def create_app():
    app = Flask(__name__)
    load_dotenv()
    CORS(app)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
    app.secret_key = os.getenv("SECRET_KEY")

    jwt = JWTManager(app)
    db.init_app(app)

    migrate = Migrate(app, db)
    migrate.init_app(app, db)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    app.register_blueprint(auth_blueprint)
    # app.register_blueprint(main_blueprint)

    return app

