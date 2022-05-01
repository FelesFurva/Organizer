def test_deletion_of_existing_task(client, prepare_data, prepare_user, login_user):
    response = client.delete("/task/7777", follow_redirects = True)
    assert 204 == response.status_code


def test_deletion_of_not_existing_task(client, prepare_user, login_user):
    response = client.delete("/task/1111", follow_redirects = True)
    assert 404 == response.status_code
