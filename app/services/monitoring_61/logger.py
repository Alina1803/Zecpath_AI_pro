import logging

logging.basicConfig(filename="logs/system.log", level=logging.INFO)


def write_log(message):

    logging.info(message)
