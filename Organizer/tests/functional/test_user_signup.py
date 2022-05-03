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
def test_create_user(username, email, password, code, isnumber, client, user_manager):
    user = {
        "username": username,
        "email": email,
        "password": password,
    }
    response = client.post("/signup", json=user)
    assert code == response.status_code
    if code == 200:
        response = client.post("/login", json={"email": email, "password": password})
        assert 401 == response.status_code
    user_id = user_manager.get_id_by_username(username)
    if user_id:
        user_manager.delete(user_id)