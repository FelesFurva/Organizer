import pytest

testdata = [
    (33333, "Charlly", 201),
    (1111, "Charlly", 404)
]

@pytest.mark.parametrize("id,newusername,code", testdata)
def test_edit_of_existing_user(id, newusername, code, client, prepare_user, login_user):
    response = client.put(
        f'/user/{id}', json={"username": newusername}, follow_redirects=True
    )
    assert code == response.status_code
