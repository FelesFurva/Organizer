def test_edit_of_existing_user(client):
    response = client.put("/user/33333", json={"username": "Charlly"})
    assert 201 == response.status_code


def test_edit_of_not_existing_user_none(client):
    response = client.put("/user/1111", json={"username": "not there"})
    assert 404 == response.status_code
