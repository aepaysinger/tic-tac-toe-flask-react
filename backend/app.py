from flask import request, escape
from models import Game
from main import app




@app.route("/")
def practice():
    name = request.args.get("name", "go")
    game = Game(whos_turn="x", board="a,b,c", winner="o")
    
    return f"Let's {escape(name)}!"