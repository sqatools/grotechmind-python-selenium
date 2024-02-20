"""
pip install pytest

# pytest command to execute the code
 python -m pytest .\test_smoke_suite.py

 # command for verbose output, which means shows more information while executing the test cases.
 python -m pytest -v .\test_smoke_suite.py

 # command to execute test case with specific marker mentioned in the test file.
  python -m pytest -v -m smoke .\tests\
"""
import pytest


@pytest.mark.smoke
def test_addition_regression():
    num1 = 10
    num2 = 30
    assert num1 + num2 == 40


@pytest.mark.sanity
def test_multiplication_regression():
    num1 = 10
    num2 = 30
    assert num1 * num2 == 301


@pytest.mark.regression
def test_division_regression():
    num1 = 10
    num2 = 30
    assert num2 // num1 == 3
