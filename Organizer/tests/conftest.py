import pytest
from flask import Flask
from project import create_app, db
from project.models import Task


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
def prepare_data(app):
    task2 = Task(id=2, task="to be deleted")
    task3 = Task(id=3, task="to be edited")    
    db.session.add(task2)
    db.session.add(task3)
    db.session.commit()
