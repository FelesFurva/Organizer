def test_edit_of_existing_user(client, login_user):
    response = client.put("/user/33333", json={"username": "Charlly"}, follow_redirects = True)
    assert 201 == response.status_code


def test_edit_of_not_existing_user_none(client, login_user):
    response = client.put("/user/1111", json={"username": "not there"}, follow_redirects = True)
    assert 404 == response.status_code
