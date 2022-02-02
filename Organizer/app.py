"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(120), nullable=False)
    

    def __repr__(self):
        return f"{self.task}"


@app.route('/')
def hello():
    """Renders a sample page."""
    return "Hello World!"

@app.route('/tasks')
def get_tasks():
    """Rebders the list of tasks"""
    tasks = Task.query.all()

    output = []
    for task in tasks:
        task_data = {'ToDo':task.task}
        
        output.append(task_data)

    return {"Tasks": output}

@app.route('/tasks', methods=['POST'])
def add_task():
    task = Task(name=request.json['task'])
    db.session.add(task)
    db.session.commit()
    return {'id': task.id}

@app.route('/tasks/<id>', methods=['DELETE'])
def delete_task(id):
    
    task = Task.query.get(id)
    if task is None:
        return {"error": "not found"}
    db.session.delete(task)
    db.session.commit()
    return {"message": "yeet"}


if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
