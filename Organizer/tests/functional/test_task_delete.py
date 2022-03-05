import unittest

def test_delete_task(client):
    response = client.delete("/task/2")
    assert 204 == response.status_code

def test_delete_task(client):
    response = client.delete("/task/1111111")
    assert 404 == response.status_code

