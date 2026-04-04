import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    PROJECT_NAME = "Zecpath AI"
    VERSION = "1.0.0"

    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./zecpath.db")

    RESUME_MODEL_VERSION = "resume_v1.0"
    ATS_MODEL_VERSION = "ats_v1.0"
    INTERVIEW_MODEL_VERSION = "interview_v1.0"
    TEST_MODEL_VERSION = "test_v1.0"

    RAW_DATA_PATH = "data/raw"
    PROCESSED_DATA_PATH = "data/processed"


settings = Settings()