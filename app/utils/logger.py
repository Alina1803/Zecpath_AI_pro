import logging
import os

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "app.log")


def get_logger(name="ZECPATH_AI_PRO"):
    logger = logging.getLogger(name)

    if not logger.handlers:
        logger.setLevel(logging.INFO)

        # File handler
        file_handler = logging.FileHandler(LOG_FILE)

        # Console handler
        console_handler = logging.StreamHandler()

        # Format (includes logger name 👇)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger


# Create logger
logger = get_logger()


# Helper function
def log(message):
    logger.info(message)