from pydantic import BaseModel

class CandidateRequest(BaseModel):
    name: str
    gender: str
    email: str
    score: int
    consent: bool