from flask import session


def test_logout(client, user):
    with client: 
        assert 'user_id' not in session
