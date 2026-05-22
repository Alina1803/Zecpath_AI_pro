import logging
import traceback
import time

from app.core.language_tool_manager import (
    get_language_tool
)


# =========================================================
# LOGGER
# =========================================================

logger = logging.getLogger(__name__)


# =========================================================
# VALIDATE LANGUAGETOOL
# =========================================================

def validate_language_tool(tool):

    if tool is None:

        logger.warning(
            "⚠️ LanguageTool Not Available "
            "→ Running In Fallback Mode"
        )

        return False

    return True


# =========================================================
# SAFE LANGUAGETOOL INIT
# =========================================================

def safe_initialize_language_tool():

    start_time = time.time()

    try:

        logger.info(
            "🚀 Initializing LanguageTool..."
        )

        tool = get_language_tool()

        is_valid = validate_language_tool(
            tool
        )

        elapsed = round(
            time.time() - start_time,
            2
        )

        if is_valid:

            logger.info(
                f"✅ LanguageTool Ready "
                f"({elapsed}s)"
            )

        else:

            logger.warning(
                f"⚠️ LanguageTool Disabled "
                f"({elapsed}s)"
            )

        return tool

    except Exception:

        logger.exception(
            "❌ LanguageTool Startup Failed"
        )

        return None


# =========================================================
# APPLICATION STARTUP
# =========================================================

def initialize_services():

    logger.info(
        "=" * 60
    )

    logger.info(
        "🚀 APPLICATION STARTUP INITIALIZED"
    )

    logger.info(
        "=" * 60
    )

    startup_start = time.time()

    try:

        # =================================================
        # LANGUAGETOOL
        # =================================================

        tool = safe_initialize_language_tool()

        # =================================================
        # FUTURE SERVICES
        # =================================================
        #
        # initialize_database()
        # initialize_redis()
        # initialize_vector_store()
        # initialize_llm_service()
        #
        # =================================================

        total_time = round(
            time.time() - startup_start,
            2
        )

        logger.info(
            "=" * 60
        )

        logger.info(
            f"✅ ALL SERVICES INITIALIZED "
            f"({total_time}s)"
        )

        logger.info(
            "=" * 60
        )

        return {

            "status": "success",

            "language_tool": (
                "enabled"
                if tool
                else "fallback"
            ),

            "startup_time_seconds":
                total_time
        }

    except Exception as e:

        logger.exception(
            "❌ APPLICATION STARTUP FAILED"
        )

        print("\n" + "=" * 60)

        print(
            "APPLICATION STARTUP FAILED"
        )

        print("=" * 60)

        print(
            f"ERROR TYPE: {type(e).__name__}"
        )

        print(
            f"ERROR MESSAGE: {str(e)}"
        )

        print("\nTRACEBACK:\n")

        traceback.print_exc()

        print("=" * 60 + "\n")

        return {

            "status": "failed",

            "error_type":
                type(e).__name__,

            "error_message":
                str(e)
        }


# =========================================================
# MANUAL TEST
# =========================================================

if __name__ == "__main__":

    result = initialize_services()

    print(result)