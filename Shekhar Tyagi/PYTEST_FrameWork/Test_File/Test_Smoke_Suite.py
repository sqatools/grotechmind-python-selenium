"""
# pytest command to execute the code
 python -m pytest .\Test_Smoke_Suite.py

 # command for verbose output, which means shows more information while executing the tests cases.
 python -m pytest -v .\Test_Smoke_Suite.py

 # command to execute tests case with specific marker mentioned in the tests file.
  python -m pytest -v -m smoke .\Test_File\

"""
import pytest

@pytest.mark.smoke
def test_addition():
	num1 = 10
	num2 = 20
	assert num1 + num2 == 30

@pytest.mark.sanity
def test_multi():
	num1 = 10
	num2 = 20
	assert num1 * num2 == 200



