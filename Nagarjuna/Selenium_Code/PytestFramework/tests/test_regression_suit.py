import pytest

@pytest.mark.smoke
def test_addition():
    num1=20
    num2=40
    assert num1 + num2 == 60

@pytest.mark.sanity
def test_multiplication():
    num1=20
    num2=40
    assert num1 * num2 == 810

@pytest.mark.regression
def test_division():
    num1=20
    num2=40
    assert num2 // num1 == 2


#python -m pytest -v -m smoke .\tests\
