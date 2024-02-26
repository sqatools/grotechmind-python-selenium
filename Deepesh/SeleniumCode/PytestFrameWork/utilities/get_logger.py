import logging
import datetime
import os

dir_name = datetime.datetime.now().strftime("logs_%Y_%m_%d_%H_%M_%S")
log_dir_path = f"./logs/{dir_name}"
os.mkdir(log_dir_path)
log_file_name = f"execution_{dir_name}.log"
log_file_path = os.path.join(log_dir_path, log_file_name)

logging.basicConfig(filename=log_file_path,
                    format="%(asctime)s [%(levelname)s] %(filename)s:%(lineno)s %(message)s",
                    level=logging.INFO,
                    filemode="a+")

logger = logging.getLogger(__name__)
