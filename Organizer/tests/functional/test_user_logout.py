from project.models import User


def test_logout(client):
    user = {"email": "c@d.com", "password": "123456"}
    client.post("/login", json=user, follow_redirects=True)
    response = client.get("/logout", follow_redirects=True)
    assert response.status_code == 200
    assert not isinstance(client, User)
