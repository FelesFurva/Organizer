from numbers import Number


def test_user_login_post(client):
    user = {"email": "c@d.com", "password": "123456"}
    response = client.post("/login", json=user)
    assert 200 == response.status_code
    assert isinstance(response.json["id"], Number)


def test_user_login_missing_email(client):
    user = {"email": "", "password": "123456"}
    response = client.post("/login", json=user)
    assert 401 == response.status_code


def test_user_login_missing_password(client):
    user = {"email": "c@d.com", "password": ""}
    response = client.post("/login", json=user)
    assert 401 == response.status_code
