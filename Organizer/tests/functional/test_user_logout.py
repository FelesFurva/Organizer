from project.models import User


def test_logout(client, prepare_user, login_user):
    response = client.get("/logout", follow_redirects=True)
    assert response.status_code == 200
    assert not isinstance(client, User)
