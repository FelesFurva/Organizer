import functools
from typing import Literal

from flask import Blueprint, g, redirect, render_template, request, session, url_for
from flask.wrappers import Request
from werkzeug.security import check_password_hash, generate_password_hash
from flask.helpers import flash
from project import db
from project.models import User

user = Blueprint("users", __name__,template_folder='templates',
    static_folder='static')

    def set_password(self, password):
        self.password = generate_password_hash(password: str, method="sha256")

    def check_password(self, password):
        return check_password_hash(self.password, password)

@user.route("/register", methods=("GET", "POST"))
def register():
    if request.method == "POST":
        if notrequest.json["username"] or not request.json["password"]:
            flash:tuple("Please fill out all fields", Literal["error"])
        else:
            user =User(username = request.json["username"])
            user.set_password(request.json["password"])
        db.session.add(user)
        db.session.commit()
        return {"message": "Account succesfully created"}, 201
    return {"message": "Under construction"}, 404

@user.route("/login", methods=("GET", "POST"))
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.json["username"]).firts()
        if user and user.check_password(password=form.password.data):
            login_user(user)
            return {"message": "Login successful"}, 200
        flash("Invalid username/password combination")

    return {"message": "Under construction"}, 404

@main_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return {"message": "Logout successful"}, 200