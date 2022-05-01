from numbers import Number


def test_create_task(client, prepare_user, login_user):
    response = client.post("/task", json={"task": "first todo"}, follow_redirects=True)
    assert 201 == response.status_code
    assert isinstance(response.json["id"], Number)
