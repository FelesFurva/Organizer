from datetime import datetime

from project import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    completed = db.Column(db.Boolean, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def __repr__(self):
        return f"{self.task} - {self.created_at} - {self.completed}"


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f"{self.email} - {self.password_hash} - {self.username}"