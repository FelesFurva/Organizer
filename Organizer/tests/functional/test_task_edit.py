

def test_edit_of_existing_task(client):
    response = client.put("/task/3", json = {"task": "first todo edited"})
    assert 201 == response.status_code

def test_edit_of_not_existing_task_none(client):
    response = client.put("/task/1111", json = {"task": "whatever"})
    assert 404 == response.status_code
