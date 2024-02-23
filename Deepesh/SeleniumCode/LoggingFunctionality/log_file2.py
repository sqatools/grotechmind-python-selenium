import logging

logging.basicConfig(filename="test_execution.log", level=logging.INFO, filemode="a", format='%(asctime)s - %('
                                                                                            'filename)s- %(name)s - '
                                                                                            '%(levelname)s -%(message)s')

logging.info("Test cases execution is failed.")
