from flask import session

from project.models import User

def test_logout(client, user):
    with client:
        
        assert 'user_id' not in session