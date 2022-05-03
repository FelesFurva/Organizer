from flask import Blueprint, request
from flask_login import login_user, logout_user
from flask_login.utils import login_required, current_user
from project import db
from project.models import User
from werkzeug.security import check_password_hash, generate_password_hash

auth = Blueprint("auth", __name__)


@auth.route("/signup", methods=["POST"])
def signup():
    email = request.json["email"]
    username = request.json["username"]
    password = request.json["password"]

    if (
        not request.json["username"]
        or not request.json["password"]
        or not request.json["email"]
    ):
        return {"message": "Please fill out all fields"}, 404
    else:
        user = User.query.filter_by(email=email).first()

        user = User(
            username=username,
            password_hash=generate_password_hash(password, method="sha256"),
            email=email,
        )

    db.session.add(user)
    db.session.commit()
    return {"username": user.username, "message": "Account successfully created"}, 201


@auth.route("/login", methods=["POST"])
def login():
    email = request.json["email"]
    password = request.json["password"]

    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password_hash, password):
        return {"message": "Invalid username/password combination"}, 401
    login_user(user)
    return {"username": user.username, "message": "Login successful"}, 200


@auth.route("/user", methods=["PUT"])
@login_required
def edit_user():

    username = request.json.get("username")
    if not username or not username.strip():
        return {"message": "input new username"}, 400

    user = User.query.get_or_404(current_user.id)
    user.username = username
    db.session.commit()

    return {"username": user.username}, 201


@auth.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return {"message": "Logout successful"}, 200


@auth.route("/user", methods=["DELETE"])
@login_required
def delete_user():

    user = User.query.get_or_404(current_user.id)

    db.session.delete(user)
    db.session.commit()
    return {"message": "User removed"}, 204
