import pytest


@pytest.fixture(scope="function")
def setup():
    print("\n tests started")
    yield
    print("\n tests completed")





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
