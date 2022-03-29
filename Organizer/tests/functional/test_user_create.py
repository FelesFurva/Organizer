from numbers import Number


def test_user_create_post(client):
    response = client.post("/register", json={"Account succesfully created"})
    assert 201 == response.status_code
    assert isinstance(response.json["id"], Number)


def test_user_create_get(client):
    response = client.get("/register")
    assert 404 == response.status_code
