import pytest
@pytest.mark.smoke
def test_addition_feature2():
    num1 = 40
    num2 = 10
    assert num1+num2 == 50
@pytest.mark.regression
def test_multiplication_feature2():
        num1 = 40
        num2 = 10
        assert num1 * num2 == 50
