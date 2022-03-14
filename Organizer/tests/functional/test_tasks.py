

def test_get_tasks(client):
    response = client.get("/tasks")
    assert response.status_code == 200