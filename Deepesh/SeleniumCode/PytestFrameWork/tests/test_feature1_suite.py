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
#from utilities.log_config import get_logger
import datetime

import logging

dir_name = datetime.datetime.now().strftime("logs_%Y_%m_%d_%H_%M_%S")
log_dir_path = f"./logs/{dir_name}"
os.mkdir(log_dir_path)
log_file_name = f"execution_{dir_name}.log"
log_file_path = os.path.join(log_dir_path, log_file_name)

logging.basicConfig(filename=log_file_path,
                    format="%(asctime)s [%(levelname)s] %(filename)s:%(lineno)s %(message)s",
                    level=logging.INFO,
                    filemode="a+")

log = logging.getLogger(__name__)
#log.info("Hello")



@pytest.mark.regression
def test_division_regression(setup):
    num1 = 10
    num2 = 30
    print("Val of num1 and num2 :", num1, num2)
    assert num2 // num1 == 3
