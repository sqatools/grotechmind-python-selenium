import logging
import os

cur_dir = os.getcwd()
log_path = os.path.join(cur_dir, 'logs')
if not os.path.isdir(log_path):
    os.mkdir(log_path)
log_file_path = os.path.join(log_path, "execution.log")
logging.basicConfig(filename=log_file_path, level=logging.INFO, filemode="a+", format='%(asctime)s - %('
                                                                                            'filename)s- %(name)s - '
                                                                                            '%(levelname)s -%(message)s')
logger = logging.getLogger(__name__)

logger.info("Hello")