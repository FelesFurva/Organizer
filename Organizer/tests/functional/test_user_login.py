import pytest

testdata = [
    ("c@d.com", "123456", 200, True),
    ("c@d.com", "", 401, False),
    ("", "123456", 401, False),
    ("", "", 401, False),
]

@pytest.mark.parametrize("email,password,code,isnumber", testdata)
def test_user_login_post(email, password, code, isnumber, client, prepare_user):
    response = client.post("/login", json={"email": email, "password": password})
    assert code == response.status_code
