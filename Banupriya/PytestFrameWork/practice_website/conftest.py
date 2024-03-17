"""
# command to run all test cases
python -m pytest -v .\tests\test_dummy.py --html-report=report.html

# command to run specific test case
python -m pytest -v .\tests\test_dummy.py::TestDummyticketbooking::test_depart_return --html-report=report.html

# command to run test with markers.
python -m pytest -v -m smoke .\tests\test_dummy.py --html-report=report.html
"""

import pytest
from selenium import  webdriver
from test_datafile import *


@pytest.fixture(scope="function")
def initial_setup():
    print("\n Test begins")
    yield
    print("\n End of the test")


@pytest.fixture(scope="session")
def browser():
    #driver = webdriver.Edge()
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver