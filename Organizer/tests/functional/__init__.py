from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_filename=None):
     app = Flask(__name__, instance_relative_config=True)

     from project.routes.hello import hello
     from project.routes.tasks import tasks
 
     app.register_blueprint(hello)
     app.register_blueprint(tasks)

     return app