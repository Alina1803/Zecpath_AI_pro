from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class ResumeBase(BaseModel):
    candidate_id: str
    skills: List[str]
    experience_years: Optional[int] = 0
    education: Optional[str] = None


class ResumeCreate(ResumeBase):
    pass