from datetime import datetime
from sqlalchemy.orm import Session

from app.services.parsers.resume_parser import parse_resume
from app.services.ats_scoring import calculate_ats_score
from app.services.interview_scoring import score_interview

from app.db import crud
from config.settings import settings

class Orchestrator:

    def _init_(self):
        print("Pipeline initialized")

    def run(self):
        print("Pipeline running...")

    def run_full_pipeline(
        self,
        candidate_id,
        name,
        email,
        resume_path,
        job_id,
        job_requirements,
        interview_transcript
    ):
        print("Running full pipeline...")

        result = {
            "candidate_id": candidate_id,
            "name": name,
            "email": email,
            "job_id": job_id,
            "resume_path": resume_path,
            "job_requirements": job_requirements,
            "interview_summary": interview_transcript[:50] + "...",
            "status": "Processed"
        }

        return result

class HiringOrchestrator:

    def __init__(self, db: Session):
        self.db = db

    # -------------------------------
    # STEP 1: Resume Parsing
    # -------------------------------
    def process_resume(self, candidate_id: str, resume_path: str):
        parsed_data = parse_resume(resume_path)

        crud.save_parsed_profile(
            db=self.db,
            candidate_id=candidate_id,
            skills=parsed_data["skills"],
            experience=parsed_data["experience_years"],
            education="Not Extracted"  # placeholder
        )

        return parsed_data

    # -------------------------------
    # STEP 2: ATS Scoring
    # -------------------------------
    def process_ats(self, candidate_id: str, job_id: str, parsed_resume: dict, job_requirements: dict):
        ats_result = calculate_ats_score(parsed_resume, job_requirements)

        crud.save_ats_score(
            db=self.db,
            candidate_id=candidate_id,
            job_id=job_id,
            scores=ats_result
        )

        return ats_result

    # -------------------------------
    # STEP 3: Interview Scoring
    # -------------------------------
    def process_interview(self, candidate_id: str, transcript: str):
        interview_result = score_interview(transcript)

        crud.save_interview_score(
            db=self.db,
            candidate_id=candidate_id,
            scores=interview_result
        )

        return interview_result

        # Create candidate entry
        crud.create_candidate(
            db=self.db,
            candidate_id=candidate_id,
            name=name,
            email=email
        )

        # Resume
        parsed_resume = self.process_resume(candidate_id, resume_path)

        # ATS
        ats_result = self.process_ats(
            candidate_id,
            job_id,
            parsed_resume,
            job_requirements
        )

        # Interview
        interview_result = self.process_interview(
            candidate_id,
            interview_transcript
        )

        # Aggregate Final Score
        final_score = (
            0.5 * ats_result["final_ats_score"] +
            0.5 * interview_result["final_interview_score"]
        )

        return {
            "candidate_id": candidate_id,
            "job_id": job_id,
            "ats_score": ats_result,
            "interview_score": interview_result,
            "final_hiring_score": round(final_score, 2),
            "model_versions": {
                "resume_model": settings.RESUME_MODEL_VERSION,
                "ats_model": settings.ATS_MODEL_VERSION,
                "interview_model": settings.INTERVIEW_MODEL_VERSION
            },
            "processed_at": datetime.utcnow()
        }