from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class ParsedResumeSchema(BaseModel):
    candidate_id: str
    skills: List[str]
    experience_years: Optional[int]
    education: Optional[str]
    model_version: str
    created_at: datetime


class ATSScoreSchema(BaseModel):
    candidate_id: str
    job_id: str
    skill_match_score: float
    experience_score: float
    final_ats_score: float
    model_version: str
    created_at: datetime


class InterviewScoreSchema(BaseModel):
    candidate_id: str
    sentiment_score: float
    confidence_score: float
    communication_score: float
    final_interview_score: float
    model_version: str
    created_at: datetime