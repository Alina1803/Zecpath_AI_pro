import time
from app.services.edge_case_31.logging.error_logger import log_error

MAX_RETRIES = 3

def retry_process(func, *args):
    for attempt in range(MAX_RETRIES):
        try:
            return func(*args)
        except Exception as e:
            log_error("RetryError", f"Attempt {attempt+1}: {str(e)}")
            time.sleep(2 ** attempt)

    raise Exception("Max retries exceeded")