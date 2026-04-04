from pydantic import BaseModel
from typing import List, Optional


class JobRequirement(BaseModel):
    job_id: str
    role: str
    required_skills: List[str]
    optional_skills: Optional[List[str]] = []
    min_experience_years: Optional[int] = 0
    education_required: Optional[str] = None