from fastapi import APIRouter
from app.models.schemas44 import StartRequest, AnswerRequest
from app.services.doc_api_44.question_engine import generate_questions

router = APIRouter()

sessions = {}
 
@router.post("/start")
def start_interview(data: StartRequest):
    session_id = "S123"

    questions = generate_questions(data.role_type)

    sessions[session_id] = {
        "candidate_id": data.candidate_id,
        "answers": []
    }

    return {
        "session_id": session_id,
        "questions": questions
    }

@router.post("/answer")
def submit_answer(data: AnswerRequest):
    sessions[data.session_id]["answers"].append(data.answer)

    return {
        "follow_up": "Can you explain more?",
        "next_question": "Describe teamwork experience"
    }