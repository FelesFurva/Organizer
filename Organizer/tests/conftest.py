import pytest
from flask import Flask
from project import create_app, db
from project.models import Task, User


@pytest.fixture()
def app():
    app: Flask = create_app("flask_test.cfg")
    app.config.update({"TESTING": True})
    with app.app_context():
        yield app


@pytest.fixture()
def client(app: Flask):
    return app.test_client()

@pytest.fixture(scope='module')
def new_user():
    user = User('testuser@gmail.com', 'testpassword')
    return user

@pytest.fixture()
def prepare_data(app):
    db.session.query(User).filter(User.id == 55555).delete()
    db.session.query(User).filter(User.id == 33333).delete()
    db.session.commit()
    user55555 = User(id=55555, user="to be deleted")
    user33333 = User(id=33333, user="to be edited")
    db.session.add(user55555)
    db.session.add(user33333)
    db.session.commit()
    yield

@pytest.fixture()
def auth(client):
    return AuthActions(client)


@pytest.fixture()
def prepare_data(app):
    db.session.query(Task).filter(Task.id == 7777).delete()
    db.session.query(Task).filter(Task.id == 3333).delete()
    db.session.commit()
    task7777 = Task(id=7777, task="to be deleted")
    task3333 = Task(id=3333, task="to be edited")
    db.session.add(task7777)
    db.session.add(task3333)
    db.session.commit()
    yield
