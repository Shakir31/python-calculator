import pytest
from calculator import add, subtract, multiply, divide


@pytest.mark.not_slow
def test_add():
    assert add(1, 1) == 2
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


@pytest.mark.not_slow
def test_subtract():
    assert subtract(2, 1) == 1
    assert subtract(0, 1) == -1
    assert subtract(0, 0) == 0


@pytest.mark.not_slow
def test_multiply():
    assert multiply(2, 2) == 4
    assert multiply(1, 0) == 0
    assert multiply(-5, 2) == -10


# marked as slow just to test the workflow
@pytest.mark.slow
def test_divide():
    assert divide(4, 2) == 2
    assert divide(2, 2) == 1
    assert divide(-10, 2) == -5


@pytest.mark.edge
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
