from fastapi import FastAPI, UploadFile, File
import shutil
import uuid
from datetime import datetime

from app.db.database import SessionLocal
from app.db.models import Candidate, ATSScore, InterviewResult

from app.services.parser import parse_resume
from app.services.scoring import score_candidate
from app.services.transcriber import transcribe_audio
from app.services.interview_ai import evaluate_interview

from app.utils.dataset import save_dataset

app = FastAPI()

RESUME_DIR = (r"E:\Zecpath_AI_pro\data\raw")
AUDIO_DIR = "storage-audio"


# 🔷 Resume Upload API
@app.post("/upload-resume/")
async def upload_resume(file: UploadFile = File(...)):
    db = SessionLocal()

    try:
        candidate_id = str(uuid.uuid4())
        file_path = f"{RESUME_DIR}{candidate_id}.pdf"

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        parsed_data = parse_resume(file_path)
        score = score_candidate(parsed_data)

        # Save candidate
        candidate = Candidate(
            candidate_id=candidate_id,
            name=parsed_data.get("name"),
            parsed_data=parsed_data
        )
        db.add(candidate)

        # Save score
        ats = ATSScore(
            candidate_id=candidate_id,
            job_id="J001",
            score=score,
            model_version="v1.0"
        )
        db.add(ats)

        db.commit()

        # Save dataset
        save_dataset({
            "candidate_id": candidate_id,
            "parsed_data": parsed_data,
            "score": score
        })

        return {
            "candidate_id": candidate_id,
            "score": score
        }

    except Exception as e:
        db.rollback()
        return {"error": str(e)}

    finally:
        db.close()

    # 🔷 Interview Upload API
@app.post("/upload-interview/")
async def upload_interview(file: UploadFile = File(...)):
    db = SessionLocal()

    try:
        interview_id = str(uuid.uuid4())
        file_path = f"{AUDIO_DIR}{interview_id}.wav"

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        transcript = transcribe_audio(file_path)
        evaluation = evaluate_interview(transcript)

        db_result = InterviewResult(
            candidate_id="UNKNOWN",
            transcript=transcript,
            scores=evaluation,
            model_version="interview_v1",
            timestamp=datetime.utcnow()
        )

        db.add(db_result)
        db.commit()

        return {
            "interview_id": interview_id,
            "transcript": transcript,
            "evaluation": evaluation
        }

    except Exception as e:
        db.rollback()
        return {"error": str(e)}

    finally:
        db.close()