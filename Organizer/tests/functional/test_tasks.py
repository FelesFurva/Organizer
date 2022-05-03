from datetime import datetime

import pytest

testdata = [
    ([{
        "ToDo" : "to be edited",
        "Created": datetime.now().strftime("%Y-%m-%d"),
        "status" : False,
        "id" : 3333
    }], 200),
    ([], 200)
]

@pytest.mark.parametrize("tasks, code", testdata)
def test_get_tasks(tasks, code, client, prepare_task_list, prepare_user, login_user):
    prepare_task_list(tasks)
    response = client.get("/tasks", follow_redirects=True)
    assert code == response.status_code
    assert tasks == response.json["Tasks"]
    