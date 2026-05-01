from pydantic import BaseModel
from typing import List, Optional


class Answer(BaseModel):
    question_id: str
    relevance_score: Optional[float] = 0.7
    communication_score: Optional[float] = 70
    confidence_score: Optional[float] = 70
    contradiction: Optional[bool] = False
    is_vague: Optional[bool] = False


class HRRequest(BaseModel):
    candidate_id: str
    candidate_type: str = "fresher"
    answers: List[Answer]