from project import db
from project.models import User
from werkzeug.security import generate_password_hash

class UserManager(object):
    """description of class"""

    def create(self, id, username, email, password):
        user = User(
            id = id,
            username = username,
            email = email,
            password_hash=generate_password_hash(password, method="sha256"),
        )
        db.session.add(user)
        db.session.commit()

    def get_id_by_username(self, username):
        user = User.query.filter_by(username = username).first()
        if user:
            return user.id

    def delete(self, id):
        db.session.query(User).filter(User.id == id).delete()
        db.session.commit()