from project import db
from project.models import Task

class TaskManager(object):
    """description of class"""
    def create(self, id, task, user_id):
        task = Task(
            id = id,
            task = task,
            user_id = user_id
        )
        db.session.add(task)
        db.session.commit()
        return id

    def delete(self, id):
        db.session.query(Task).filter(Task.id == id).delete()
        db.session.commit()

    def delete_all(self):
        db.session.query(Task).delete()
        db.session.commit()