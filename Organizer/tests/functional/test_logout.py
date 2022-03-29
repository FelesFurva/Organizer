from flask import session


def test_logout(client):
    with client: 
        assert 'user_id' not in session
