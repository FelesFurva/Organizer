import unittest



def test_edit_task(client):
    response = client.put("/task/2", json = { "task": "first todo edited" })
    assert 201 == response.status_code