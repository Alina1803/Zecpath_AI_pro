from app.services.recommendation_ai_52.decision_engine import generate_decision
from app.services.recommendation_ai_52.risk_engine import apply_risk_penalty
from app.services.recommendation_ai_52.confidence_engine import calculate_confidence
from app.services.recommendation_ai_52.explanation_engine import generate_explanation


def recommendation_pipeline(candidate_id, scores, behavior_risk, integrity_risk):

    final_score = scores.get("final_score", 0)

    adjusted_score = apply_risk_penalty(final_score, behavior_risk, integrity_risk)

    decision = generate_decision(adjusted_score)

    confidence = calculate_confidence(list(scores.values()))

    explanation = generate_explanation(scores)

    return {
        "candidate_id": candidate_id,
        "final_score": final_score,
        "adjusted_score": adjusted_score,
        "decision": decision,
        "confidence_score": confidence,
        "risks": {"behavior": behavior_risk, "integrity": integrity_risk},
        "explanation": explanation,
    }
