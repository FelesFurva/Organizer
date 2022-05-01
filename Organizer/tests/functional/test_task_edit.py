def test_edit_of_existing_task(client, prepare_user, login_user):
    response = client.put("/task/3333", json={"task": "first todo edited"}, follow_redirects = True)
    assert 201 == response.status_code


def test_edit_of_not_existing_task_none(client, prepare_user, login_user):
    response = client.put("/task/1111", json={"task": "whatever"}, follow_redirects = True)
    assert 404 == response.status_code
