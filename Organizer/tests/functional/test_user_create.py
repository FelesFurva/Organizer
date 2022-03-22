from numbers import Number


def test_user_create(client):
    response = client.post("/register", json={"Account succesfully created"})
    assert 201 == response.status_code
    assert isinstance(response.json["id"], Number)
