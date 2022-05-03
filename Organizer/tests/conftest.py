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
def prepare_data(task_manager):
    task_manager.create(7777, "to be deleted", 33333)
    task_manager.create(3333, "to be edited", 33333)
    yield
    task_manager.delete(7777)
    task_manager.delete(3333)


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
