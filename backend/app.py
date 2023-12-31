import os

from dotenv import load_dotenv
from flask_cors import CORS
from flask_migrate import Migrate
from db import db
from flask import Flask
from main_bp import main as main_blueprint
from auth import auth as auth_blueprint
from flask_login import LoginManager
from models import User


def create_app():
    app = Flask(__name__)
    load_dotenv()
    cors = CORS(app)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.secret_key = os.getenv("SECRET_KEY")
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
    app.register_blueprint(main_blueprint)

    return app
