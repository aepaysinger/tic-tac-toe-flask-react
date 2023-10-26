import json

from datetime import datetime, timedelta, timezone
from flask import Blueprint, flash, jsonify, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, unset_jwt_cookies, jwt_required, JWTManager

from db import db
from models import Detail, User




auth = Blueprint("auth", __name__)


# old login
@auth.route("/login1", methods=["POST"])
def login_post():
    email = request.form.get("email")
    password = request.form.get("password")
    remember = True if request.form.get("remember") else False

    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        flash("Please check your login details and try again.")
        return redirect(url_for("auth.login"))
    login_user(user, remember=remember)
    return redirect(url_for("main.profile"))


@auth.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_login = create_access_token(identity=get_jwt_identity())
            data = response.get_json()
            if type(data) is dict:
                data["access_login"] = access_login
                response.data = json.dumps(data)
        return response
    except (RuntimeError, KeyError):
        return response
    

# sign up?
@auth.route('/token', methods=['POST'])
def create_token():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        return {"msg": "Please check your login details and try again."}, 401
    access_token = create_access_token(identity=email)
    response = {"access_token":access_token}
    return response

# old sign up
@auth.route("/signup", methods=["POST", "GET"])
def signup_post():
    if request.method == "GET":
        return render_template("signup.html")
    email = request.form.get("email")
    name = request.form.get("name")
    password = request.form.get("password")

    user = User.query.filter_by(email=email).first()

    if user:
        flash("Email address already exists")
        return redirect(url_for("auth.login"))
    new_user = User(
        email=email,
        name=name,
        password=generate_password_hash(password, method="sha256"),
    )
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for("auth.login"))


@auth.route("/logout", methods=["POST"])
def logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response

# old details
@auth.route("/details", methods=["POST"])
def get_details():
    data = request.json
    user = User.query.get_or_404(data["user_id"])
    detail = Detail(info=data["info"], user=user)
    db.session.add(detail)
    db.session.commit()
    return "okay", 200


@auth.route('/profile', methods=['GET'])
@jwt_required()
def my_profile():
    response_body = {
        "name": "Nagato",
        "about" :"Hello! I'm a full stack developer that loves python and javascript"
    }
    
    return response_body