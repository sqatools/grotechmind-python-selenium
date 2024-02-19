import pytest

@pytest.mark.sanity
def test_addition():
    num1=10
    num2=5
    assert num1+num2==15
@pytest.mark.smoke
def test_multiplication():
    num1=40
    num2=5
    assert num1*num2==200
@pytest.mark.sanity
def test_division():
    num1=40
    num2=5
    assert num1//num2==8
@pytest.mark.smoke
def test_subtraction():
    num1=40
    num2=20
    assert num1-num2==20

#python -m pytest .\test_smoke_suite.py
#python -m pytest -v .\test_smoke_suite.py
