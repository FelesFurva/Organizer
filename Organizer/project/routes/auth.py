from functools import wraps

from flask import Blueprint, Request
from flask_login import login_user, logout_user
from project import db
from project.models import User
from werkzeug.security import check_password_hash, generate_password_hash

auth = Blueprint("auth", __name__)


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if User.query.get(id) is None:
            return {"message": "user id is none"}
        return f(*args, **kwargs)

    return decorated_function


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if Request.method == "POST":

        email=Request.json["email"]
        username=Request.json["username"]
        password=Request.json["password"]
        
        if not Request.json["username"] or not Request.json["password"] or not Request.json["email"]:
            return {"message": "Please fill out all fields"}
        else:
            user = User.query.filter_by(email=email).first()
            if user:
                return {"message": "User already exists"}
            new_user = User(username=username, password_hash=generate_password_hash(password, method="sha256"), email=email)

        db.session.add(new_user)
        db.session.commit()
        return {"id": user.id, "message": "Account succesfully created"}, 201
    return {"message": "Under construction"}, 404


@auth.route("/login", methods=["GET", "POST"])
def login(id):
    if Request.method == "POST":
        email = Request.json["email"]
        password = Request.json["password"]

        user = User.query.filter_by(email=email).firts()
        if not user or not check_password_hash(user.password_hash, password):
            return {"message": "Invalid username/password combination"}
        login_user(user)
        return {"message": "Login successful"}, 200
    return {"message": "Under construction"}, 404


@auth.route("/logout")
@login_required
def logout():

    logout_user()
    return {"message": "Logout successful"}, 200


@auth.route("/user/<id>", methods=["DELETE"])
def delete_user(id):

    user = User.query.get_or_404(id)

    db.session.delete(user)
    db.session.commit()
    return {"message": "User removed"}, 204
