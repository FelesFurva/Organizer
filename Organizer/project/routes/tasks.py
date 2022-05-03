from flask import Blueprint, request
from flask_login.utils import login_required, current_user
from project import db
from project.models import Task

tasks = Blueprint("tasks", __name__)


@tasks.route("/tasks")
@login_required
def get_tasks():

    """Reads the list of tasks"""

    tasks = Task.query.filter_by(user_id = current_user.id)

    output = []
    for task in tasks:
        task_data = {
            "ToDo": task.task,
            "Created": task.created_at.strftime("%Y-%m-%d"),
            "status": task.completed,
            "id": task.id,
        }

        output.append(task_data)

    return {"Tasks": output}, 200


@tasks.route("/task", methods=["POST"])
@login_required
def add_task():
    """Creates a new task"""
    task = Task(task=request.json["task"], user_id = current_user.id)

    db.session.add(task)
    db.session.commit()

    return {"id": task.id, "created": task.created_at.strftime("%Y-%m-%d")}, 201

@tasks.route("/task/<id>", methods=["GET"])
@login_required
def get_task_byid(id):
    task = Task.query.filter_by(user_id = current_user.id, id = id).first()

    return {"id": task.id, "task": task.task, "status": task.completed}, 200

@tasks.route("/task/<id>", methods=["PUT"])
@login_required
def edit_task(id):
    """Updates a task"""

    task = Task.query.filter_by(user_id = current_user.id, id = id).first()
    if not task:
        return {"message": "Not found"}, 404
    task.task = request.json.get("task", task.task)

    db.session.commit()
    return {"id": task.id, "edited task": task.task, "updated": task.updated_at}, 202


@tasks.route("/task/<id>", methods=["DELETE"])
@login_required
def delete_task(id):
    """Deletes a task by id"""

    task = Task.query.filter_by(user_id = current_user.id, id = id).first()
    if not task:
        return {"message": "Not found"}, 404

    db.session.delete(task)
    db.session.commit()
    return {"message": "yeet"}, 204
