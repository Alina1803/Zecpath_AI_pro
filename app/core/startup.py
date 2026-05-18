import logging
import traceback

from app.core.language_tool_manager import (get_language_tool)

# =========================================================
# LOGGER
# =========================================================

logger = logging.getLogger(__name__)

# =========================================================
# VALIDATE SERVICES
# =========================================================

def validate_language_tool(tool):

    if tool is None:

        logger.error(
            "❌ LanguageTool Initialization Returned None")

        raise RuntimeError(
            "LanguageTool failed to initialize")


# =========================================================
# STARTUP SERVICES
# =========================================================

def initialize_services():

    logger.info(
        "🚀 Initializing Application Services..."
    )

    try:

        # =================================================
        # LANGUAGETOOL INITIALIZATION
        # =================================================

        logger.info(
            "🚀 Starting LanguageTool Service..."
        )

        tool = get_language_tool()

        validate_language_tool(tool)

        logger.info(
            "✅ LanguageTool Service Ready"
        )

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

        logger.info(
            "✅ All Application Services Initialized")

    except Exception as e:

        logger.exception(
            "❌ FULL STARTUP ERROR BELOW")

        print("\n" + "=" * 60)
        print("APPLICATION STARTUP FAILED")
        print("=" * 60)

        print(f"ERROR TYPE: {type(e).__name__}")
        print(f"ERROR MESSAGE: {str(e)}")

        print("\nTRACEBACK:\n")

        traceback.print_exc()

        print("=" * 60 + "\n")

        raise