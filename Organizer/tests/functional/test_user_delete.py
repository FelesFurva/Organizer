def test_deletion_of_existing_user(client, prepare_user, login_user):
    response = client.delete("/user/55555")
    assert 204 == response.status_code


def test_deletion_of_not_existing_user(client, login_user):
    response = client.delete("/user/1111", follow_redirects=True)
    assert 404 == response.status_code
