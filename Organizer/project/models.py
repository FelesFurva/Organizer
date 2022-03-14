from project import db
from datetime import datetime


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    completed = db.Column(db.Boolean, default=0)
    
    def __repr__(self):
        return f"{self.task} - {self.created_at} - {self.completed}"
