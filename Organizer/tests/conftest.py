import pytest
from flask import Flask
from project import create_app, db
from project.models import Task, User
from werkzeug.security import generate_password_hash

from utils.UserManager import UserManager
from utils.TaskManager import TaskManager


@pytest.fixture()
def app():
    app: Flask = create_app("flask_test.cfg")
    app.config.update({"TESTING": True})
    with app.app_context():
        yield app


@pytest.fixture()
def client(app: Flask):
    return app.test_client()

@pytest.fixture()
def login_user(client):
    user = {"email": "c@d.com", "password": "123456"}
    response = client.post("/login", json=user, follow_redirects=True)
    yield response

@pytest.fixture()
def user_manager():
    return UserManager()

@pytest.fixture()
def prepare_user(user_manager):
    user_manager.create(55555, "to_be_deleted", "a@b.com", "123456")
    user_manager.create(33333, "to_be_edited", "c@d.com", "123456")
    yield
    user_manager.delete(55555)
    user_manager.delete(33333)

@pytest.fixture()
def task_manager():
    return TaskManager()

@pytest.fixture()
def prepare_task_list(prepare_task):
    def _prepare_task_list(tasks):
        task_ids = []
        for task in tasks:
            task_ids.append(prepare_task(task["id"], task["ToDo"], 33333))
        return task_ids
    yield _prepare_task_list

@pytest.fixture()
def prepare_task(task_manager):
    task_ids = []

    def _prepare_task(id, task, user_id):
        task_id = task_manager.create(id, task, user_id)
        task_ids.append(task_id)
        return task_id

    yield _prepare_task

    for task_id in task_ids:
        task_manager.delete(task_id)

@pytest.fixture(scope="session", autouse=True)
def callattr_ahead_of_alltests(request):
    print("callattr_ahead_of_alltests called")
    seen = {None}
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        if cls not in seen:
            if hasattr(cls.obj, "callme"):
                cls.obj.callme()
            seen.add(cls)
