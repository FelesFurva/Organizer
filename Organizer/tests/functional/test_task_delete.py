def test_delete_task(client, prepare_data):
    response = client.delete("/task/777")
    assert 204 == response.status_code


def test_delete_task_none(client):
    response = client.delete("/task/1111111")
    assert 404 == response.status_code
