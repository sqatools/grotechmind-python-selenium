"""
pip install pytest

# pytest command to execute the code
 python -m pytest .\test_smoke_suite.py

 # command for verbose output, which means shows more information while executing the test cases.
 python -m pytest -v .\test_smoke_suite.py

 # command to execute test case with specific marker mentioned in the test file.
  python -m pytest -v -m smoke .\tests\


Fixture function : Fixture function executes as per the scope of the test cases defined.
it initiates before the execution of the test cases and end of the test cases.

scope of the fixture
function : In this scope the fixture function executes along with each test function.
session : In this scope the fixture function will execute only once for entire execution

"""
import pytest

@pytest.fixture(scope="session")
def setup():
    print("\n test case execution started")
    yield
    print("\n test case execution completed")

@pytest.mark.smoke
def test_addition_regression(setup):
    num1 = 10
    num2 = 30
    print("Val of num1 and num2 :", num1, num2 )
    assert num1 + num2 == 40


@pytest.mark.sanity
def test_multiplication_regression(setup):
    num1 = 10
    num2 = 30
    print("Val of num1 and num2 :", num1, num2)
    assert num1 * num2 == 301


@pytest.mark.regression
def test_division_regression(setup):
    num1 = 10
    num2 = 30
    print("Val of num1 and num2 :", num1, num2)
    assert num2 // num1 == 3
