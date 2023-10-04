from flask import Blueprint, render_template
# from app import db


main = Blueprint('main', __name__)

@main.route('/index')
def index():
    return render_template('index.html')

@main.route('/profile')
def profile():
    return render_template('profile.html')