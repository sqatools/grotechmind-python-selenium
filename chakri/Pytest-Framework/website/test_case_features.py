import pytest


@pytest.fixture(scope="function")
def setup():
    print("\n test started")
    yield
    print("\n test completed")





def test_add(setup):
    a = 10
    b = 5
    assert a + b == 15


def test_multiplication(setup):
    a = 10
    b = 5
    assert a * b == 50

@pytest.mark.sanity
def test_subtraction(setup):
    a = 10
    b = 9
    assert a - b == 1
