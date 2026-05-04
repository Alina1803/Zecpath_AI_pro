from app.services.unified_scoring_engine_41.unified_scoring_engine import get_weights, calculate_unified_score
from app.services.unified_scoring_engine_41.hiring_fit import calculate_hiring_fit
from app.services.unified_scoring_engine_41.decision_engine import get_decision
from app.services.unified_scoring_engine_41.explainability import generate_explanation

def unified_pipeline(candidate_id, ats, screening, hr, role="fresher"):

    weights = get_weights(role)

    final_score = calculate_unified_score(ats, screening, hr, weights)

    decision = get_decision(final_score)

    fit = calculate_hiring_fit(final_score)

    explanation = generate_explanation({
        "ats": ats,
        "screening": screening,
        "hr": hr
    })

    return {
        "candidate_id": candidate_id,
        "scores": {
            "ats": ats,
            "screening": screening,
            "hr": hr
        },
        "weights": weights,
        "final_score": final_score,
        "decision": decision,
        "hiring_fit": fit,
        "explanation": explanation
    }