"""
# pytest command to execute the code
 python -m pytest .\test_smoke_suite.py

 # command for verbose output, which means shows more information while executing the test cases.
 python -m pytest -v .\test_smoke_suite.py

 # command to execute test case with specific marker mentioned in the test file.
  python -m pytest -v -m smoke .\tests\

"""

def test_addition():
    num1=20
    num2=40
    assert num1 + num2 == 60

def test_multiplication():
    num1=20
    num2=40
    assert num1 * num2 == 810


def test_division():
    num1=20
    num2=40
    assert num2 // num1 == 2

def test_substraction():
    num1=40
    num2=14
    assert num1-num2 == 20
