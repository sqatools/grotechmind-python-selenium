import pytest

@pytest.mark.sanity
def test_additionf1():
    num1=10
    num2=5
    assert num1+num2==15
@pytest.mark.smoke
def test_multiplicationf2():
    num1=40
    num2=5
    assert num1*num2==200
@pytest.mark.sanity
def test_divisionf3():
    num1=40
    num2=5
    assert num1//num2==8
@pytest.mark.smoke
def test_subtractionf4():
    num1=40
    num2=20
    assert num1-num2==20

#python -m pytest .\test_smoke_suite.py
#python -m pytest -v .\test_smoke_suite.py

# pytest command to execute the code
#python -m pytest .\test_smoke_suite.py

# command for verbose output, which means shows more information while executing the test cases.
#python -m pytest -v .\test_smoke_suite.py

# command to execute test case with specific marker mentioned in the test file.
#python -m pytest -v -m smoke .\tests\

#marker
#python -m pytest -v -m smoke .\test_regression_suite.py  .\test_smoke_suite.py
