import pytest
from tests.conftest import task_manager

testdata = [
    ({"ToDo" : "to be edited", "id" : 3333}, "first todo edited", 202)
]

@pytest.mark.parametrize("task, edited_task, code", testdata)
def test_edit_of_existing_task(task, edited_task, code, client, prepare_task, task_manager, prepare_user, login_user):
    task_id = prepare_task(task["id"], task["ToDo"], 33333)
    response = client.get(f"/task/{task_id}")
    assert 200 == response.status_code
    assert "to be edited" == response.json["task"]
    response2 = client.put(
        f"/task/{task_id}", json={"task": edited_task}, follow_redirects=True
    )
    assert code == response2.status_code
    assert edited_task == task_manager.get_task_by_id(task_id).task

def test_edit_of_not_existing_task_none(client, prepare_user, login_user):
    response = client.put(
        "/task/1111", json={"task": "whatever"}, follow_redirects=True
    )
    assert 404 == response.status_code
