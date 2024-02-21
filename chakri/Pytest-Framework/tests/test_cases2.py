'''
# pytest command to execute the code
 python -m pytest .\test_smoke_suite.py

 # command for verbose output, which means shows more information while executing the test cases.
 python -m pytest -v .\test_smoke_suite.py

 # command to execute test case with specific marker mentioned in the test file.
  python -m pytest -v -m smoke .\tests\
'''


def test_addition():
    a = 10
    b = 20
    assert a + b == 30


def test_sub():
    a = 10
    b = 5
    assert a-b == 5


def test_multi():
    a = 10
    b = 4
    assert a*b == 40
