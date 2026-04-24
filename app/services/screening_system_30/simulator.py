from app.services.screening_system_30.intent_detection import predict_intent
from app.services.screening_system_30.scoring import score_candidate

def simulate_call(user_input):
    intent = predict_intent(user_input)
    score = score_candidate(user_input)

    result = {
        "input": user_input,
        "intent": intent,
        "score": score,
        "status": "Accepted" if score >= 2 else "Rejected"
    }

    return result