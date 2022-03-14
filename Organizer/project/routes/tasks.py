from flask import Blueprint, request
from project import db
from project.models import Task

tasks = Blueprint("tasks",__name__)


@tasks.route("/tasks")
def get_tasks():
    
    """Reads the list of tasks"""    

    tasks = Task.query.all()

    output = []
    for task in tasks:
        task_data = {
            "ToDo":task.task,
            "Created":task.created_at,
            "status":task.completed,
            "id": task.id
        }
        
        output.append(task_data)

    return {"Tasks": output}


@tasks.route('/task', methods=["POST"])
def add_task():
    """Creates a new task"""

    task = Task(task=request.json["task"])

    db.session.add(task)
    db.session.commit()

    return {"id": task.id, "created": task.created_at}, 201

@tasks.route('/task/<id>', methods=["PUT"])
def edit_task(id):
    """Updates a task"""

    task = Task.query.get_or_404(id)  
    task.task = request.json.get("task", task.task)

    db.session.commit()
    return {"id": task.id, "edited task": task.task, "updated": task.updated_at}, 201

@tasks.route('/task/<id>', methods=["DELETE"])
def delete_task(id):
    """Deletes a task by id"""
    
    task = Task.query.get_or_404(id)

    db.session.delete(task)
    db.session.commit()
    return {"message": "yeet"}, 204
