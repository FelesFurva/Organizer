"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    completed = db.Column(db.Boolean, default=0)

    def __repr__(self):
        return f"{self.task} - {self.created_at} - {self.completed}"


@app.route('/')
def hello():
    """Renders a sample page."""
    return "Hello World!"

"""Rebders the list of tasks"""
@app.route('/tasks')
def get_tasks():
    
    tasks = Task.query.all()

    output = []
    for task in tasks:
        task_data = {'ToDo':task.task, 'Created':task.created_at, 'status':task.completed, 'id': task.id}
        
        output.append(task_data)

    return {"Tasks": output}

# create a new task
@app.route('/task', methods=['POST'])
def add_task():
    task = Task(task=request.json['task'])

    db.session.add(task)
    db.session.commit()

    return {'id': task.id, 'created': task.created_at}, 201

# edit a task
@app.route('/task/<id>', methods=['PUT'])
def edit_task(id):

    task = Task.query.get(id)

    upd_task = request.json['task']
    
    task.task = upd_task 
       
    if task is None:
        return {"error": "not found"}
    
    
    db.session.commit()
    return {'id': task.id, 'edited task': task.task, 'updated': task.updated_at}, 200

# delete a task by id
@app.route('/task/<id>', methods=['DELETE'])
def delete_task(id):
    
    task = Task.query.get(id)
    if task is None:
        return {"error": "not found"}
    db.session.delete(task)
    db.session.commit()
    return {"message": "yeet"}, 204


if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
