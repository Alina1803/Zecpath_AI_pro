import time
import logging
from functools import wraps

logging.basicConfig(filename="logs/app.log", level=logging.INFO)

def track_time(func):
    """
    Decorator to measure execution time
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()
        duration = end - start

        logging.info(f"{func.__name__} executed in {duration:.4f} seconds")
        print(f"{func.__name__} executed in {duration:.4f} seconds")

        return result

    return wrapper