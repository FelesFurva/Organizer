from numbers import Number


def test_create_task(client, task_manager, prepare_user, login_user):
    response = client.post("/task", json={"task": "first todo2"}, follow_redirects=True)
    assert 201 == response.status_code
    created_id = response.json["id"]
    assert isinstance(created_id, Number)
    task_manager.delete(created_id)


def test_create_task_noauth(client, prepare_user):
    response = client.post("/task", json={"task": "first todo failed"}, follow_redirects=True)
    assert 401 == response.status_code
