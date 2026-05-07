from pydantic import BaseModel
from typing import List, Optional


# -----------------------------------
# Answer Schema
# -----------------------------------
class Answer(BaseModel):
    question: str
    answer: str


# -----------------------------------
# Demo Request Schema
# -----------------------------------
class DemoRequest(BaseModel):
    candidate_id: str
    answers: Optional[List[Answer]] = []


# -----------------------------------
# Score Schema
# -----------------------------------
class ScoreResponse(BaseModel):
    communication: float
    confidence: float
    aptitude: float
    hr: float
    ats: float
    screening: float


# -----------------------------------
# Summary Schema
# -----------------------------------
class SummaryResponse(BaseModel):
    strengths: List[str]
    weaknesses: List[str]
    cultural_fit: str


# -----------------------------------
# Final Interview Result Schema
# -----------------------------------
class InterviewResult(BaseModel):
    candidate_id: str
    scores: ScoreResponse
    final_score: float
    decision: str
    summary: SummaryResponse


# -----------------------------------
# Report Response Schema
# -----------------------------------
class ReportResponse(BaseModel):
    candidate_id: str
    status: str
    message: str