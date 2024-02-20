"""
pip install pytest

# pytest command to execute the code
 python -m pytest .\test_smoke_suite.py
 python -m pytest -v .\test_smoke_suite.py
"""


def test_addition_regression():
    num1 = 10
    num2 = 30
    assert num1 + num2 == 40


def test_multiplication_regression():
    num1 = 10
    num2 = 30
    assert num1 * num2 == 301


def test_division_regression():
    num1 = 10
    num2 = 30
    assert num2 // num1 == 3
