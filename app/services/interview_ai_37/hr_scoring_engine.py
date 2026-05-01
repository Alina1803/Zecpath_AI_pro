"""
HR Scoring Engine
-----------------
Core logic for scoring HR interview answers
"""

# -------------------------------
# Default Weights
# -------------------------------
DEFAULT_WEIGHTS = {
    "relevance": 0.30,
    "communication": 0.25,
    "confidence": 0.25,
    "consistency": 0.20
}


# -------------------------------
# Consistency Score
# -------------------------------
def score_consistency(answer):
    if answer.get("contradiction"):
        return 0.3
    if answer.get("is_vague"):
        return 0.6
    return 1.0


# -------------------------------
# Per Answer Scoring
# -------------------------------
def score_hr_answer(answer, weights=DEFAULT_WEIGHTS):
    relevance = answer.get("relevance_score", 0.7)
    communication = answer.get("communication_score", 70) / 100
    confidence = answer.get("confidence_score", 70) / 100
    consistency = score_consistency(answer)

    final = (
        relevance * weights["relevance"] +
        communication * weights["communication"] +
        confidence * weights["confidence"] +
        consistency * weights["consistency"]
    )

    return {
        "question_id": answer.get("question_id"),
        "scores": {
            "relevance": round(relevance, 2),
            "communication": round(communication, 2),
            "confidence": round(confidence, 2),
            "consistency": round(consistency, 2)
        },
        "final_score": round(final * 100, 2)
    }


# -------------------------------
# Aggregate Score
# -------------------------------
def aggregate_hr_scores(scored_answers):
    if not scored_answers:
        return 0

    total = sum(a["final_score"] for a in scored_answers)
    return round(total / len(scored_answers), 2)


# -------------------------------
# HR Pipeline
# -------------------------------
from app.services.interview_ai_37.hr_weights import get_weights


def hr_scoring_pipeline(answers, candidate_type="fresher"):
    weights = get_weights(candidate_type)

    scored = []
    for ans in answers:
        result = score_hr_answer(ans, weights)
        scored.append(result)

    final_score = aggregate_hr_scores(scored)

    decision = (
        "Strong Hire" if final_score >= 75 else
        "Consider" if final_score >= 55 else
        "Reject"
    )

    return {
        "hr_score": final_score,
        "decision": decision,
        "details": scored
    }