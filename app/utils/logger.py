import logging
import os

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(LOG_DIR, "app.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

<<<<<<< HEAD
logger = logging.getLogger("Zecpath_AI_pro")
=======
logger = logging.getLogger("zecpath_ai")
>>>>>>> f3c0930173c3eaf45f856e918e2731922b901711
