import os
import json

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import demo45, report45

# -----------------------------------
# FastAPI App Initialization
# -----------------------------------
app = FastAPI(
    title="HR Interview AI - Final System",
    version="1.0.0",
    description="Production-ready HR Interview AI using FastAPI"
)

# -----------------------------------
# Enable CORS
# -----------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------------
# Include Routes
# -----------------------------------
app.include_router(demo45.router, prefix="/api/v1", tags=["Demo"])
app.include_router(report45.router, prefix="/api/v1", tags=["Report"])

# -----------------------------------
# Create Output Directory
# -----------------------------------
OUTPUT_DIR = "data/processed/output_45"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# -----------------------------------
# Root Endpoint
# -----------------------------------
@app.get("/")
def root():

    output_data = {
        "message": "HR AI Running",
        "status": "Production Ready"
    }

    # Save output file
    output_path = os.path.join(
        OUTPUT_DIR,
        "day45_output.json"
    )

    with open(output_path, "w") as file:
        json.dump(output_data, file, indent=4)

    return output_data


# -----------------------------------
# Health Check Endpoint
# -----------------------------------
@app.get("/health")
def health_check():
    return {
        "status": "OK",
        "system": "HR Interview AI"
    }