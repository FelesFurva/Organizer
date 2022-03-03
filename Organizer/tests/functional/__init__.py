import unittest


import pytest

from flask import Flask
from project import create_app, db

@pytest.fixture()
def app():
    app: Flask = create_app('flask_test.cfg')
    app.config.update({"TESTING": True})    
    yield app

@pytest.fixture()
def client(app: Flask):
    return app.test_client()
