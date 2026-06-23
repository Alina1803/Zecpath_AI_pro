import json
import logging
import time
import traceback

from contextlib import asynccontextmanager
from datetime import datetime
from pathlib import Path

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import Request

from fastapi.middleware.cors import CORSMiddleware

from fastapi.responses import JSONResponse

from app.core.config import settings

from app.services.demo_45.final_hr_engine import FinalHRInterviewSystem

from app.api.routes.health_routes45 import router as health_router

# =========================================================
# LOGGING CONFIGURATION
# =========================================================

logging.basicConfig(
    level=logging.INFO,
    format=("%(asctime)s | " "%(levelname)s | " "%(name)s | " "%(message)s"),
)

logger = logging.getLogger(__name__)

# =========================================================
# GLOBAL ENGINE CACHE
# =========================================================

HR_ENGINE = None

# =========================================================
# OUTPUT DIRECTORY
# =========================================================

OUTPUT_DIR = Path(settings.OUTPUT_DIR)

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# =========================================================
# APPLICATION LIFECYCLE
# =========================================================


@asynccontextmanager
async def lifespan(app: FastAPI):

    global HR_ENGINE

    try:

        logger.info("\n=================================")
        logger.info("API STARTUP INITIALIZED")
        logger.info("=================================")

        if HR_ENGINE is None:

            logger.info("Loading Final HR Interview Engine...")

            HR_ENGINE = FinalHRInterviewSystem()

            logger.info("✅ HR Interview Engine Ready")

        else:

            logger.info("✅ Reusing Existing Engine")

        logger.info("✅ API Startup Completed")

        yield

    except Exception as e:

        logger.error(f"❌ Startup Failed : {str(e)}")

        logger.error(traceback.format_exc())

        raise e

    finally:

        logger.info("\n=================================")
        logger.info("API SHUTDOWN")
        logger.info("=================================")


# =========================================================
# FASTAPI APPLICATION
# =========================================================

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    debug=settings.DEBUG,
    lifespan=lifespan,
)

# =========================================================
# CORS
# =========================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================================================
# ROUTERS
# =========================================================

app.include_router(health_router, prefix=settings.API_PREFIX)

# =========================================================
# REQUEST LOGGER MIDDLEWARE
# =========================================================


@app.middleware("http")
async def request_logger(request: Request, call_next):

    start_time = time.time()

    logger.info(f"📥 Request : " f"{request.method} " f"{request.url.path}")

    try:

        response = await call_next(request)

    except Exception as e:

        logger.error(f"❌ Middleware Error : {str(e)}")

        logger.error(traceback.format_exc())

        return JSONResponse(
            status_code=500,
            content={"status": "failed", "message": ("Internal Server Error")},
        )

    process_time = round(time.time() - start_time, 2)

    logger.info(f"📤 Response Status : " f"{response.status_code}")

    logger.info(f"⏱ Processing Time : " f"{process_time} sec")

    return response


# =========================================================
# SAVE OUTPUT JSON
# =========================================================


def save_output(data: dict):

    try:

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        file_path = OUTPUT_DIR / (f"interview_output_{timestamp}.json")

        with open(file_path, "w", encoding="utf-8") as file:

            json.dump(data, file, indent=4, ensure_ascii=False)

        logger.info(f"✅ Output Saved : {file_path}")

        return str(file_path)

    except Exception as e:

        logger.error(f"❌ Output Save Failed : {e}")

        logger.error(traceback.format_exc())

        return None


# =========================================================
# ROOT ROUTE
# =========================================================


@app.get("/")
async def root():

    return {
        "application": settings.APP_NAME,
        "version": settings.VERSION,
        "status": "running",
        "docs": "/docs",
    }


# =========================================================
# HEALTH ROUTE
# =========================================================


@app.get("/health")
async def health_check():

    return {"status": "healthy", "engine_loaded": (HR_ENGINE is not None)}


# =========================================================
# START INTERVIEW
# =========================================================


@app.post("/start-interview")
async def start_interview():

    global HR_ENGINE

    try:

        logger.info("\n=================================")
        logger.info("🚀 INTERVIEW PIPELINE STARTED")
        logger.info("=================================")

        if HR_ENGINE is None:

            logger.warning("⚠ Engine Cache Empty")

            HR_ENGINE = FinalHRInterviewSystem()

        result = HR_ENGINE.start_interview(
            candidate_id="CAND_001", role="backend developer", experience="experienced"
        )

        output_path = save_output(result)

        logger.info("✅ Interview Completed")

        return JSONResponse(
            status_code=200,
            content={
                "status": "success",
                "message": ("Interview Completed"),
                "output_path": output_path,
                "data": result,
            },
        )

    except Exception as e:

        logger.error(f"❌ Interview Failed : {str(e)}")

        logger.error(traceback.format_exc())

        raise HTTPException(status_code=500, detail=("Interview Processing Failed"))


# =========================================================
# MAIN ENTRY
# =========================================================

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        "app.api.main_api45:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.DEBUG,
        workers=1,
        log_level="info",
    )
