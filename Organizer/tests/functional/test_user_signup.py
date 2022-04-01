from numbers import Number


def test_user_create_post(client):
    response = client.post("/signup")
    assert 201 == response.status_code
    assert isinstance(response.json["id"], Number)
