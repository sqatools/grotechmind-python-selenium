import pytest

"""
# pytest command to execute the code
 python -m pytest .\test_smoke_suite.py

 # command for verbose output, which means shows more information while executing the test cases.
 python -m pytest -v .\test_smoke_suite.py

 # command to execute test case with specific marker mentioned in the test file.
  python -m pytest -v -m smoke .\tests\

"""

@pytest.mark.smoke
def test_addition_feature1():
    num1=20
    num2=40
    assert num1 + num2 == 60

@pytest.mark.sanity
def test_multiplication_feature1():
    num1=20
    num2=40
    assert num1 * num2 == 810

@pytest.mark.regression
def test_division_feature1():
    num1=20
    num2=40
    assert num2 // num1 == 2


# for running only the sanity in the tests we need to specify by sanity
# python -m pytest -v -m sanity .\tests\
