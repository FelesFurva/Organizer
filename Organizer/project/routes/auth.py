from functools import wraps

from flask import Flask, Blueprint, request
from flask_login import login_user, logout_user
from project import db
from project.models import User
from werkzeug.security import check_password_hash, generate_password_hash

auth = Blueprint("auth", __name__)


#def login_required(f):
#    @wraps(f)
#    def decorated_function(*args, **kwargs):
#        if User.query.get(id) is None:
#            return {"message": "user id is none"}
#        return f(*args, **kwargs)

#    return decorated_function


@auth.route("/signup", methods=["POST"])
def signup():


        user = User(username=request.json["username"], password_hash=generate_password_hash(request.json["password"], method="sha256"), email=request.json["email"])

        db.session.add(user)
        db.session.commit()
        return {"id": user.id}, 201


@auth.route("/login", methods=["POST"])
def login():
    
        password = request.json["password"]

        user = User.query.filter_by(email=request.json["email"]).firts()
        if not user or not check_password_hash(user.password_hash, password):
            return {"message": "Invalid username/password combination"}
        login_user(user)
        return {"message": "Login successful"}, 200

@auth.route("/user/<id>", method=["PUT"])
def edit_user(id):

    user = User.query.get_or_404(id)
    user.user = request.json.get("username", user.username)

    db.session.commit()

    return {"id": user.id, "username": user.username}, 201

@auth.route("/logout", methods=["GET"])
#@login_required
def logout():
    logout_user()
    return {"message": "Logout successful"}, 200


@auth.route("/user/<id>", methods=["DELETE"])
def delete_user(id):

    user = User.query.get_or_404(id)

    db.session.delete(user)
    db.session.commit()
    return {"message": "User removed"}, 204
