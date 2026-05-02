from app.config.scoring_weights40 import WEIGHTS
from app.services.hr_simulation_40.confidence_detector import detect_confidence
from app.services.hr_simulation_40.communication_analyzer import communication_score

def relevance_score(answer):
    return 80 if len(answer) > 10 else 60

def consistency_score(answer):
    return 75  # placeholder

def calculate_score(answer):
    scores = {
        "relevance": relevance_score(answer),
        "communication": communication_score(answer),
        "confidence": detect_confidence(answer),
        "consistency": consistency_score(answer)
    }

    final_score = sum(scores[k] * WEIGHTS[k] for k in WEIGHTS)
    return round(final_score, 2)