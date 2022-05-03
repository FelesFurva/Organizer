import pytest
from tests.conftest import task_manager

testdata = [
    ({"ToDo" : "to be deleted", "id" : 7777}, 204),
    (None, 404)
]

@pytest.mark.parametrize("task, code", testdata)
def test_deletion_of_existing_task(task, code, client, task_manager, prepare_task, prepare_user, login_user):
    if task:
        task_id = prepare_task(task["id"], task["ToDo"], 33333)
    else:
        task_id = -1
    response = client.delete(f"/task/{task_id}", follow_redirects=True)
    assert code == response.status_code
