import logging
import os


def get_logger():
    cur_dir = os.getcwd()
    log_dir = os.path.join(cur_dir, 'logs')
    if not os.path.isdir(log_dir):
        os.mkdir(log_dir)
    log_path = os.path.join(cur_dir, log_dir)
    log_file_path = os.path.join(log_path, 'execution.log')
    logging.basicConfig(filename=log_file_path,
                        format='%(asctime)s - %(filename)s- %(name)s - %(levelname)s -%(message)s',
                        level=logging.INFO,
                        filemode="a+"
                        )
    logger = logging.getLogger(__name__)
    return logger

#get_logger().info("Hello")
