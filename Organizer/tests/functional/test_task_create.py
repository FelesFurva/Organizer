
from numbers import Number


def test_create_task(client):
    response = client.post("/task", json={"task": "first todo"})
    assert 201 == response.status_code
    assert isinstance(response.json["id"], Number)