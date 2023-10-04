# from app import db
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
class Game(db.Model):
    __tablename__ = "games"

    game_id = db.Column(db.Integer, primary_key=True)
    whos_turn = db.Column(db.String(1), unique=False, nullable=False)
    board = db.Column(db.String(), unique=False, nullable=False)
    winner = db.Column(db.String(), unique=False, nullable=False)
