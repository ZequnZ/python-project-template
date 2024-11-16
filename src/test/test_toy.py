import pytest


def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4


def test_fixture(example_data):
    assert example_data == [1, 2, 3]


@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 54)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected
