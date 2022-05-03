def test_edit_of_existing_task(client, prepare_data, prepare_user, login_user):
    response = client.get("/task/3333")
    assert 200 == response.status_code
    assert "to be edited" == response.json["task"]
    response2 = client.put(
        "/task/3333", json={"task": "first todo edited"}, follow_redirects=True
    )
    assert 202 == response2.status_code
    response3 = client.get("/task/3333")
    assert 200 == response3.status_code
    assert "first todo edited" == response3.json["task"]


def test_edit_of_not_existing_task_none(client, prepare_user, login_user):
    response = client.put(
        "/task/1111", json={"task": "whatever"}, follow_redirects=True
    )
    assert 404 == response.status_code
