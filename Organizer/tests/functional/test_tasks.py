def test_get_tasks(client, prepare_user, login_user):
    response = client.get("/tasks", follow_redirects=True)
    assert response.status_code == 200
