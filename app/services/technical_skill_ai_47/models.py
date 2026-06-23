from pydantic import BaseModel


class AnswerRequest(BaseModel):
    answer: str
    difficulty: str = "basic"
    is_correct: bool = True
