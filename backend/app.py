import os

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

load_dotenv()
app = Flask(__name__)
cors = CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv["DATABASE_URL"]

db = SQLAlchemy(app)

class TicTacToe(db.Model):
    __tablename__ = "Games"

    game_id = db.Column(db.Integer, primary_key=True)
    whos_turn = db.Column(db.String(1), unique=False, nullable=False)
    board = db.Column(db.String(), unique=False, nullabe=False)
    winner = db.Column(db.string(), unique=False, nullable=False)


if __name__ == "__main__":
    app.run()