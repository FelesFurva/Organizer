import pytest
from flask import Flask
from project import create_app, db
from project.models import Task, User
from werkzeug.security import generate_password_hash


@pytest.fixture()
def app():
    app: Flask = create_app("flask_test.cfg")
    app.config.update({"TESTING": True})
    with app.app_context():
        yield app


@pytest.fixture()
def client(app: Flask):
    return app.test_client()


@pytest.fixture(scope="module")
def new_user():
    user = User("testuser@gmail.com", "testpassword")
    return user


@pytest.fixture()
def login_user(client):
    user = {"email": "c@d.com", "password": "123456"}
    response = client.post("/login", json=user, follow_redirects=True)
    yield response


@pytest.fixture()
def delete_all_users():
    db.session.query(User).delete()
    db.session.commit()
    yield


@pytest.fixture()
def prepare_user():
    db.session.query(User).filter(User.id == 55555).delete()
    db.session.query(User).filter(User.id == 33333).delete()
    db.session.commit()
    user55555 = User(
        id=55555,
        username="to be deleted",
        email="a@b.com",
        password_hash=generate_password_hash("123456", method="sha256"),
    )
    user33333 = User(
        id=33333,
        username="to be edited",
        email="c@d.com",
        password_hash=generate_password_hash("123456", method="sha256"),
    )
    db.session.add(user55555)
    db.session.add(user33333)
    db.session.commit()
    yield


@pytest.fixture()
def prepare_data():
    db.session.query(Task).filter(Task.id == 7777).delete()
    db.session.query(Task).filter(Task.id == 3333).delete()
    db.session.commit()
    task7777 = Task(id=7777, task="to be deleted", user_id = 33333)
    task3333 = Task(id=3333, task="to be edited", user_id = 33333)
    db.session.add(task7777)
    db.session.add(task3333)
    db.session.commit()
    yield


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
