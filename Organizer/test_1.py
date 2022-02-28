import unittest
from numbers import Number

class Test_test_1(unittest.TestCase):
    def test_A(self):
        self.fail("Not implemented")

if __name__ == '__main__':
    unittest.main()

def test_create_task(client):
    response = client.post("/task", json = { "task": "first todo" })
    assert 201 == response.status_code
    assert isinstance(response.json["id"], Number)
