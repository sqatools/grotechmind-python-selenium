
import pytest

@pytest.mark.regression
def test_addition():
	num1 = 10
	num2 = 20
	assert num1+num2 ==30

@pytest.mark.retast
def test_multi():
	num1 = 10
	num2 = 20
	assert num1 * num2 == 200

@pytest.mark.smoke
def test_div():
	num1 = 10
	num2 = 20
	assert num2 // num1 == 2

