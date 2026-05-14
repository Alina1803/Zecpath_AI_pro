import os
import json

from datetime import datetime
from fastapi import FastAPI

from app.services.demo_45.final_hr_engine import (FinalHRInterviewSystem)

from app.api.routes.health_routes45 import (router as health_router)

# =====================================================
# FASTAPI APP
# =====================================================

app = FastAPI(
    title="HR Interview AI",
    version="45.0.0"
)

# =====================================================
# INCLUDE ROUTERS
# =====================================================

app.include_router(
    health_router
)

# =====================================================
# OUTPUT DIRECTORY
# =====================================================

OUTPUT_DIR = os.path.join(
    "data",
    "processed",
    "output_45"
)

os.makedirs(
    OUTPUT_DIR,
    exist_ok=True
)

# =====================================================
# SAVE OUTPUT
# =====================================================

def save_output(data):

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    file_path = os.path.join(
        OUTPUT_DIR,
        f"interview_output_{timestamp}.json"
    )

    with open(file_path, "w") as f:

        json.dump(
            data,
            f,
            indent=4
        )

    print(
        f"\nOutput Saved: {file_path}"
    )

    return file_path

# =====================================================
# HOME ROUTE
# =====================================================

@app.get("/")

def home():

    return {
        "message": "Production HR Interview AI Running",
        "version": "45.0.0",
        "status": "active"
    }

# =====================================================
# START INTERVIEW ROUTE
# =====================================================

@app.post("/start-interview")

def start_interview():

    try:

        # =================================
        # LOAD ENGINE ONLY WHEN API CALLED
        # =================================

        engine = (
            FinalHRInterviewSystem()
        )

        # =================================
        # START INTERVIEW
        # =================================

        result = (
            engine.start_interview(
                candidate_id="CAND_001",
                role="backend developer",
                experience="experienced"
            )
        )

        # =================================
        # SAVE OUTPUT
        # =================================

        output_path = save_output(
            result
        )

        # =================================
        # API RESPONSE
        # =================================

        return {
            "status": "success",
            "output_path": output_path,
            "data": result
        }

    except Exception as e:

        print(
            f"\nInterview API Failed: {e}"
        )

        return {
            "status": "failed",
            "error": str(e)
        }

# =====================================================
# RUN SERVER
# =====================================================

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        "app.api.main_api45:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )