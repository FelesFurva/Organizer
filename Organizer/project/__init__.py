from flask import Flask
import flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()


def create_app(config_filename=None):

    app = Flask(__name__, instance_relative_config=True)

    if config_filename:
        app.config.from_pyfile(config_filename)

    db.init_app(app)
    
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "users.login"
    
    
    from project.models import User

    @login_manager.user_loader
    def load_user(id):
        return User.query.filter_by(alternative_id=id).first()
    def get_id(self):
        return str(self.alternative_id)

    db.create_all(app=app)

    from project.routes.auth import auth
    from project.routes.hello import hello
    from project.routes.tasks import tasks

    app.register_blueprint(auth)
    app.register_blueprint(hello)
    app.register_blueprint(tasks)

    return app
