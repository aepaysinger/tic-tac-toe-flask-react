from flask_login import UserMixin


from db import db


class Game(db.Model):
    __tablename__ = "games"

    game_id = db.Column(db.Integer, primary_key=True)
    whos_turn = db.Column(db.String(1), unique=False, nullable=False)
    board = db.Column(db.String(), unique=False, nullable=False)
    winner = db.Column(db.String(), unique=False, nullable=False)


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class Detail(db.Model):
    __tablename__ = "details"

    id = db.Column(db.Integer, primary_key=True)
    info = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship("User", back_populates = "details")


User.details = db.relationship("Detail", order_by = Detail.id, back_populates = "user")

