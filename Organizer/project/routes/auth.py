from flask import Blueprint, request
from flask_login import login_user, logout_user
from flask_login.utils import login_required
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
            return {"message": "Please fill out all fields"}
        else:
            user = User.query.filter_by(email=email).first()

            user = User(
                username=username,
                password_hash=generate_password_hash(password, method="sha256"),
                email=email,
            )

        db.session.add(user)
        db.session.commit()
        return {"id": user.id, "message": "Account successfully created"}, 201


@auth.route("/login", methods=["POST"])
def login():
    email = request.json["email"]
    password = request.json["password"]

    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password_hash, password):
        return {"message": "Invalid username/password combination"}, 401
    login_user(user)
    return {"id": user.id, "message": "Login successful"}, 200


@auth.route("/user/<id>", methods=["PUT"])
@login_required
def edit_user(id):

    user = User.query.get_or_404(id)
    user.user = request.json.get("username", user.username)

    db.session.commit()

    return {"id": user.id, "username": user.username}, 201


@auth.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return {"message": "Logout successful"}, 200


@auth.route("/user/<id>", methods=["DELETE"])
@login_required
def delete_user(id):

    user = User.query.get_or_404(id)

    db.session.delete(user)
    db.session.commit()
    return {"message": "User removed"}, 204
