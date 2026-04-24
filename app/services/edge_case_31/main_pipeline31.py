from fastapi import FastAPI, Body
from app.services.edge_case_31.ai_flow.conversation_manager import process_user_input
from app.services.edge_case_31.logging.monitoring import track_request, get_metrics

import os
import json
from datetime import datetime
import uuid

app = FastAPI()

# Ensure output directory exists
OUTPUT_DIR = "data/processed/output_31"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Dummy AI (replace with real model)
def ai_model(text):
    return "Processed: " + text


@app.post("/process")
def process(input_text: str = Body(...)):
    track_request()

    # 🔹 Run pipeline
    response = process_user_input(input_text, ai_model)

    # 🔹 Unique filename (UUID safer than timestamp)
    file_name = f"{uuid.uuid4()}.json"
    file_path = os.path.join(OUTPUT_DIR, file_name)

    # 🔹 Save output safely
    output_data = {
        "input": input_text,
        "output": response
    }

    try:
        with open(file_path, "w") as f:
            json.dump(output_data, f, indent=4)
    except Exception as e:
        file_path = "Error saving file"

    return {
        "response": response,
        "saved_to": file_path
    }


@app.get("/metrics")
def metrics():
    return get_metrics()