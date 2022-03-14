

def test_root_request(client):
    response = client.get("/")
    assert b"Hello, World!" in response.data
