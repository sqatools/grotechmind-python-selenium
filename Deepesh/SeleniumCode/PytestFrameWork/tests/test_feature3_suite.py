"""
pip install pytest

# pytest command to execute the code
 python -m pytest .\test_smoke_suite.py
 python -m pytest -v .\test_smoke_suite.py
"""
import pytest


@pytest.mark.smoke
def test_addition_feature3():
    num1 = 10
    num2 = 30
    assert num1 + num2 == 40


@pytest.mark.sanity
def test_multiplication_feature3():
    num1 = 10
    num2 = 30
    assert num1 * num2 == 301


@pytest.mark.regression
def test_division_feature3():
    num1 = 10
    num2 = 30
    assert num2 // num1 == 3
