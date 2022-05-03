from datetime import datetime

def test_get_tasks(client, prepare_data, prepare_user, login_user):

    task = {
        "ToDo" : "to be edited",
        "Created": datetime.now().strftime("%Y-%m-%d"),
        "status" : False,
        "id" : 3333
    }

    response = client.get("/tasks", follow_redirects=True)
    assert response.status_code == 200
    assert task in response.json["Tasks"]
