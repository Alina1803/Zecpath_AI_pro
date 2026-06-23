import os
from pathlib import Path

# =========================================================
# BASE DIRECTORY
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent.parent


# =========================================================
# PROJECT CONFIGURATION
# =========================================================


class Settings:

    # =====================================================
    # APPLICATION
    # =====================================================

    APP_NAME: str = "HR Interview System"

    VERSION: str = "45.0.0"

    DEBUG: bool = True

    # =====================================================
    # API CONFIGURATION
    # =====================================================

    API_PREFIX: str = "/api"

    HOST: str = "0.0.0.0"

    PORT: int = 8000

    # =====================================================
    # LOGGING
    # =====================================================

    LOG_LEVEL: str = "INFO"

    # =====================================================
    # DIRECTORIES
    # =====================================================

    ROOT_DIR: Path = BASE_DIR

    DATA_DIR: Path = ROOT_DIR / "data"

    TEMP_DIR: Path = Path(os.getenv("APP_TEMP_DIR", "G:/temp"))

    OUTPUT_DIR: Path = DATA_DIR / "processed" / "output_45"

    # =====================================================
    # LANGUAGETOOL
    # =====================================================

    LANGUAGE: str = "en-US"

    LT_CACHE_SIZE: int = 1000

    LT_PIPELINE_CACHING: bool = True

    # =====================================================
    # INITIALIZATION
    # =====================================================

    @classmethod
    def initialize(cls) -> None:
        """
        Initialize required directories
        and environment variables.
        """

        # ================================================
        # CREATE DIRECTORIES
        # ================================================

        cls.TEMP_DIR.mkdir(parents=True, exist_ok=True)

        cls.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

        # ================================================
        # ENVIRONMENT VARIABLES
        # ================================================

        os.environ["TMPDIR"] = str(cls.TEMP_DIR)

        os.environ["TEMP"] = str(cls.TEMP_DIR)


# =========================================================
# INITIALIZE SETTINGS
# =========================================================

Settings.initialize()


# =========================================================
# GLOBAL SETTINGS OBJECT
# =========================================================

settings = Settings()
