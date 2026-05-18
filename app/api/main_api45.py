import json
import logging

from datetime import datetime
from pathlib import Path
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

from app.core.config import settings
from app.core.startup import initialize_services

from app.services.demo_45.final_hr_engine import (
    FinalHRInterviewSystem)

from app.api.routes.health_routes45 import (
    router as health_router)


# =====================================================
# LOGGING CONFIGURATION
# =====================================================

logging.basicConfig(
    level=settings.LOG_LEVEL,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s"
)

logger = logging.getLogger(__name__)


# =====================================================
# OUTPUT DIRECTORY
# =====================================================

OUTPUT_DIR = settings.OUTPUT_DIR

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)


# =====================================================
# APPLICATION LIFECYCLE
# =====================================================

@asynccontextmanager
async def lifespan(app: FastAPI):

    try:

        logger.info(
            "🚀 Starting FastAPI application..."
        )

        # =============================================
        # INITIALIZE SERVICES
        # =============================================

        initialize_services()

        logger.info(
            "✅ Application startup completed"
        )

        yield

    except Exception as e:

        logger.exception(
            f"❌ Application startup failed: {e}"
        )

        raise

    finally:

        logger.info(
            "🛑 Application shutdown completed"
        )


# =====================================================
# FASTAPI APPLICATION
# =====================================================

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    debug=settings.DEBUG,
    lifespan=lifespan
)


# =====================================================
# INCLUDE ROUTERS
# =====================================================

app.include_router(
    health_router,
    prefix=settings.API_PREFIX
)


# =====================================================
# SAVE OUTPUT
# =====================================================

def save_output(data: dict) -> str:
    """
    Save interview output as JSON.
    """

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    file_path = OUTPUT_DIR / (
        f"interview_output_{timestamp}.json"
    )

    try:

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

        logger.info(
            f"✅ Output saved: {file_path}"
        )

        return str(file_path)

    except Exception as e:

        logger.exception(
            f"❌ Failed to save output: {e}"
        )

        raise


# =====================================================
# HOME ROUTE
# =====================================================

@app.get("/")

async def home():

    return {
        "application": settings.APP_NAME,
        "version": settings.VERSION,
        "status": "running"
    }


# =====================================================
# HEALTH CHECK ROUTE
# =====================================================

@app.get("/health")

async def health_check():

    return {
        "status": "healthy"
    }


# =====================================================
# START INTERVIEW ROUTE
# =====================================================

@app.post("/start-interview")

async def start_interview():

    try:

        logger.info(
            "🚀 Starting interview pipeline..."
        )

        # =============================================
        # INITIALIZE ENGINE
        # =============================================

        engine = FinalHRInterviewSystem()

        # =============================================
        # START INTERVIEW
        # =============================================

        result = engine.start_interview(
            candidate_id="CAND_001",
            role="backend developer",
            experience="experienced"
        )

        # =============================================
        # SAVE OUTPUT
        # =============================================

        output_path = save_output(result)

        logger.info(
            "✅ Interview completed successfully"
        )

        return JSONResponse(
            status_code=200,
            content={
                "status": "success",
                "output_path": output_path,
                "data": result
            }
        )

    except Exception as e:

        logger.exception(
            f"❌ Interview pipeline failed: {e}"
        )

        raise HTTPException(
            status_code=500,
            detail="Interview processing failed"
        )


# =====================================================
# MAIN ENTRY POINT
# =====================================================

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        "app.api.main_api45:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
        workers=1,
        log_level=settings.LOG_LEVEL.lower()
    )