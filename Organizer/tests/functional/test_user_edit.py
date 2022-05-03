import pytest

testdata = [
    ("Charlly", 201),
    ("", 400),
    (" ", 400)
]

@pytest.mark.parametrize("newusername,code", testdata)
def test_edit_of_existing_user(newusername, code, client, prepare_user, login_user):
    response = client.put(
        '/user', json={"username": newusername}, follow_redirects=True
    )
    assert code == response.status_code
