import pytest
@pytest.mark.smoke
def test_addition_feature1():
    num1=10
    num2=30
    assert num1 +num2==40
@pytest.mark.sanity
def test_multiplication_feature1():
    num1=10
    num2=30
    assert num1 * num2==301


@pytest.mark.regresion
def test_division_feature1():
    num1=10
    num2=30
    assert num2 // num1==3

