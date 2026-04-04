import logging
import os
LOG_DIR = "data/logs"
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=f"{LOG_DIR}/system.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)