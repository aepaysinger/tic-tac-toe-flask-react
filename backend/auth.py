from flask import request, escape, Blueprint, render_template
from models import Game

# from app import app




# @app.route("/")
# def practice():
#     name = request.args.get("name", "go")
#     game = Game(whos_turn="x", board="a,b,c", winner="o")
    
#     return f"Let's {escape(name)}!"



auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/logout')
def logout():
    return render_template('logout.html')

@auth.route("/")
def practice():
    name = request.args.get("name", "go")
    game = Game(whos_turn="x", board="a,b,c", winner="o")
    
    return f"Let's {escape(name)}!"