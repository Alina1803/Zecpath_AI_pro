from pydantic import BaseModel
from datetime import datetime


class ATSScore(BaseModel):
    candidate_id: str
    job_id: str
    skill_match_score: float
    experience_score: float
    final_ats_score: float
    model_version: str
    created_at: datetime


class InterviewScore(BaseModel):
    candidate_id: str
    sentiment_score: float
    confidence_score: float
    communication_score: float
    final_interview_score: float
    model_version: str
    created_at: datetime


class TestScore(BaseModel):
    candidate_id: str
    mcq_score: float
    coding_score: float
    final_test_score: float
    created_at: datetime