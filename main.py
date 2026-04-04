import os
import json
from app.pipeline.orchestration import Orchestrator
from app.utils.file_manager import ensure_directories
from app.utils.helpers import generate_candidate_id
from config.settings import settings
from app.database import SessionLocal

from fastapi import FastAPI

app=FastAPI()

def main():

    # Ensure folders exist
    ensure_directories()

    # Simulated DB session placeholder
    db = SessionLocal() # Replace with real DB session later
if __name__=="__main__":
    orchestrator = Orchestrator()
    orchestrator.run()
    candidate_id = generate_candidate_id()

    result = orchestrator.run_full_pipeline(
        candidate_id=candidate_id,
        name="Alice Johnson",
        email="alice@example.com",
        resume_path="data/raw/sample_resume.pdf",
        job_id="JOB_001",
        job_requirements={
            "required_skills": ["python", "django"],
            "min_experience_years": 2
        },
        interview_transcript="I confidently developed scalable APIs using Python."
    )

    print("\nFinal Hiring Decision Output:\n")
    print(result)


if __name__ == "__main__":
    main()