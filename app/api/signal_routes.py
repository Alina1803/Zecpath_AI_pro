from fastapi import APIRouter
from app.services.signal_engine_27.signal_engine import SignalEngine

router = APIRouter()
engine = SignalEngine()


@router.post("/analyze-signal")
def analyze_signal(payload: dict):
    answer = payload.get("answer")

    result = engine.evaluate(answer)

    return {
        "status": "success",
        "data": result
    }