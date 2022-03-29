from functools import wraps
from flask import (
    Blueprint, 
    g, 
    redirect, 
    render_template, 
    request, 
    sessions,
    url_for
    )
from sqlalchemy.orm.session import Session
from project import db
from project.models import User
from werkzeug.security import check_password_hash, generate_password_hash

user = Blueprint("users", __name__,template_folder='templates',
    static_folder='static')

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if Session.get("user_id") is None:
            return redirect("/index")
        return f(*args, **kwargs)
    return decorated_function

def set_password(self, password):
    self.password = generate_password_hash((password) (str), method="sha256")

def check_password(self, password):
    return check_password_hash(self.password, password)

@user.route("/register", methods=("GET", "POST"))
def register():
    if request.method == "POST":
        if not request.json["username"] or not request.json["password"]:
            return {"message": "Please fill out all fields"}
        else:
            user =User(username = request.json["username"],  password_hash = generate_password_hash(request.json["password"]))

        db.session.add(user)
        db.session.commit()
        return {"message": "Account succesfully created"}, 201
    return {"message": "Under construction"}, 404

@user.route("/login", methods=("GET", "POST"))
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.json["username"]).firts()
        if user and user.check_password(request.json["password"]):
            Session["user_id"] = User.query.get(id)
            return {"message": "Login successful"}, 200
        return {"message": "Invalid username/password combination"}

    return {"message": "Under construction"}, 404

@user.route("/logout")
@login_required
def logout():

    Session.clear()
    return {"message": "Logout successful"}, 200
