
from numbers import Number


def test_user_create_post(client, delete_all_users):
    user = {
        "username": "Jimmy", 
        "email": "andrey@extremeautomation.io", 
        "password": "1234567890qwertY"
    }
    response = client.post("/signup", json=user)
    assert 201 == response.status_code
    assert isinstance(response.json["id"], Number)


def test_user_create_get(client):
    response = client.get("/signup")
    assert 404 == response.status_code
