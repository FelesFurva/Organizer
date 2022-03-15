def test_deletion_of_existing_task(client, prepare_data):
    response = client.delete("/task/7777")
    assert 204 == response.status_code


def test_deletion_of_not_existing_task(client):
    response = client.delete("/task/1111")
    assert 404 == response.status_code
