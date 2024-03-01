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



# to run this we need to type this line in terminal with file name
# python -m pytest .\test_smoke_suite.py

# to get details of the tests run
# python -m pytest -v .\test_smoke_suite.py
# python -m pytest -v -m .\test_smoke_suite.py .\test_regression_suite.py

# cd ..   with this we can go back path for one step
