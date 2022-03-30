from functools import wraps

from flask import Blueprint, Request
from project import db
from project.models import User
from sqlalchemy.orm.session import Session
from werkzeug.security import check_password_hash, generate_password_hash

user = Blueprint("user", __name__)


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if user = User.query.get(id) is None:
            return {"message": "user id is none"}
        return f(*args, **kwargs)

    return decorated_function


def set_password(self):
    self.password = generate_password_hash((password)(str), method="sha256")


def check_password(self):
    return check_password_hash(self.password, password)


@user.route("/register", methods=["GET", "POST"])
def register():
    if Request.method == "POST":
        if not Request.json["username"] or not Request.json["password"]:
            return {"message": "Please fill out all fields"}
        else:
            user = User(
                username=Request.json["username"],
                password_hash=generate_password_hash(Request.json["password"])
            )

        db.session.add(user)
        db.session.commit()
        return {"id": user.id, "message": "Account succesfully created"}, 201
    return {"message": "Under construction"}, 404


@user.route("/login", methods=["GET", "POST"])
def login(id):
    if Request.method == "POST":
        user = User.query.filter_by(username=Request.json["username"]).firts()
        if user and user.check_password(Request.json["password"]):
            user = User.query.get_or_404(id)
            return {"message": "Login successful"}, 200
        return {"message": "Invalid username/password combination"}

    return {"message": "Under construction"}, 404


@user.route("/logout", methods=["GET"])
@login_required
def logout():

    Session.clear()
    return {"message": "Logout successful"}, 200


@user.post("/user/<id>", , methods=["DELETE"])
def delete_user(id):

    user = User.query.get_or_404(id)

    db.session.delete(user)
    db.session.commit()
    return {"message": "User removed"}, 204
