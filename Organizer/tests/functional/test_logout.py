
from project.models import User


def test_logout(client):
    response = client.get("/logout")
    assert response.status_code == 200
    assert not isinstance(client, User)