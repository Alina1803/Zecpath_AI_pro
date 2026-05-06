from pydantic import BaseModel

class StartRequest(BaseModel):
    candidate_id: str
    job_id: str
    role_type: str
    experience_level: str

class AnswerRequest(BaseModel):
    session_id: str
    question_id: str
    answer: str
    duration: int