import json
from fastapi import FastAPI
from app.services.transcript_engine_23.processor import process_transcript
from app.services.transcript_engine_23.scoring import score_ca_answer
from app.services.transcript_engine_23.storage import save_transcript
from app.services.transcript_engine_23.repository import save_to_db


app = FastAPI(
    title="CA Transcript Engine API",
    version="1.0"
)


# ==========================
# CORE PIPELINE LOGIC
# ==========================
def run_pipeline_data(transcript: dict):
    # Process transcript
    processed = process_transcript(transcript)

    # Score CA answer
    topics = processed.get("detected_topics", [])
    processed["answer_score"] = score_ca_answer(topics)

    # Save processed JSON
    candidate_id = processed["metadata"]["candidate_id"]
    file_path = save_transcript(candidate_id, processed)

    # Save to SQLite DB
    save_to_db(processed)

    return {
        "status": "success",
        "saved_to": file_path,
        "topics": topics,
        "answer_score": processed["answer_score"],
        "data": processed
    }


def run_pipeline(input_file):
    with open(input_file, "r", encoding="utf-8") as f:
        transcript = json.load(f)

    result = run_pipeline_data(transcript)

    print(" Pipeline completed successfully")
    print(f" JSON saved to: {result['saved_to']}")
    print(f" Topics detected: {result['topics']}")
    print(f" Answer score: {result['answer_score']}")

    return result


# ==========================
# FASTAPI ROUTES
# ==========================
@app.get("/")
def home():
    return {
        "message": "CA Transcript API running",
        "module": "Day 23 Transcript Engine"
    }


@app.post("/process-transcript")
def process_transcript_api(data: dict):
    try:
        result = run_pipeline_data(data)
        return result

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }


# ==========================
# LOCAL TEST RUN
# ==========================
if __name__ == "__main__":
    input_path = "app/services/transcript_engine_23/dataset/sample_ca_transcripts.json"
    run_pipeline(input_path)