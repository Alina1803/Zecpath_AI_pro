from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class TranscriptSegment(BaseModel):
    speaker: str
    text: str
    timestamp: float
    confidence: float
    finance_skill_tags: List[str] = []

class TranscriptMetadata(BaseModel):
    candidate_id: str
    job_id: str
    question_id: str
    domain: str = "chartered_accountant"
    created_at: datetime

class Transcript(BaseModel):
    metadata: TranscriptMetadata
    segments: List[TranscriptSegment]
    detected_topics: List[str] = []
    answer_score: Optional[float] = 0.0
    compliance_accuracy: Optional[float] = 0.0
    full_text: Optional[str] = None