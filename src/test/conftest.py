import pytest


@pytest.fixture()
def example_data():
    print("before testing")
    yield [1, 2, 3]
    print("after testing")
