import pytest


def sum(a, b):
    return a + b


@pytest.mark.parametrize("num1,num2,result", [
    (1, 2, 3),
    (2, 5, 7),
    (10, 5, 15)
])
def test_sum(num1, num2, result):
    assert sum(num1, num2) == result
