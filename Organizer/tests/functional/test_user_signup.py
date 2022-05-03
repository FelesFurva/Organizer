import pytest
from numbers import Number


testdata = [
    ("Jimmy", "andrey@extremeautomation.io", "1234567890qwertY", 201, True),
    ("", "andrey@extremeautomation.io", "1234567890qwertY", 404, False),
    ("Jimmy", "", "1234567890qwertY", 404, False),
    ("Jimmy", "andrey@extremeautomation.io", "", 404, False),
    ("", "", "", 404, False),
]

@pytest.mark.parametrize("username,email,password,code,isnumber", testdata)
def test_create_user(username, email, password, code, isnumber, client, delete_all_users):
    user = {
        "username": username,
        "email": email,
        "password": password,
    }
    response = client.post("/signup", json=user)
    assert code == response.status_code
