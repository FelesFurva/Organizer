def test_deletion_of_existing_user(client):
    response = client.delete("/user/55555")
    assert 204 == response.status_code


def test_deletion_of_not_existing_user(client):
    response = client.delete("/user/1111")
    assert 404 == response.status_code
