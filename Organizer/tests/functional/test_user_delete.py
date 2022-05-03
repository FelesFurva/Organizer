def test_deletion_of_existing_user(client, prepare_user, login_user):
    response = client.delete("/user")
    assert 204 == response.status_code
