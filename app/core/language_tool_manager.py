import logging
import threading
import traceback
import shutil
import os

from functools import lru_cache

import language_tool_python

from app.core.config import settings


logger = logging.getLogger(__name__)

_tool_lock = threading.Lock()


@lru_cache(maxsize=1)
def get_language_tool():

    with _tool_lock:

        try:

            logger.info("🚀 Initializing LanguageTool...")

            # CHECK JAVA
            java_path = shutil.which("java")

            logger.info(f"Java Path: {java_path}")

            if not java_path:
                logger.error("❌ Java is NOT installed or not in PATH")
                return None

            logger.info(f"LANGUAGE = {settings.LANGUAGE}")

            tool = language_tool_python.LanguageTool(
                settings.LANGUAGE,
                config={
                    "cacheSize": settings.LT_CACHE_SIZE,
                    "pipelineCaching": settings.LT_PIPELINE_CACHING
                }
            )

            logger.info("✅ LanguageTool Initialized Successfully")

            return tool

        except Exception as e:

            logger.error("❌ FULL ERROR BELOW")
            logger.error(str(e))

            traceback.print_exc()

            return None