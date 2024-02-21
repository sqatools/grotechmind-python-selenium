import pytest


@pytest.mark.smoke
def test_addition():
    a = 10
    b = 20
    assert a + b == 30


@pytest.mark.chakri
def test_subtraction():
    a = 10
    b = 5
    assert a - b == 5


@pytest.mark.sai
def test_multi():
    a = 10
    b = 4
    assert a * b == 40
