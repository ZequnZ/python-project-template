from hello import random_output
import pytest


def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4


def test_data(example_data):
    assert example_data == [1, 2, 3]


@pytest.mark.test_mark
def test_two():
    assert 1 == 1


def test_random_output():
    assert random_output("a") == "a"
