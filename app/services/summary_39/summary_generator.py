from app.services.summary_39.decision_engine import calculate_overall_score, get_decision, build_recommendation
from app.services.summary_39.summary_templates import generate_natural_summary
from app.utils.text_formatter import format_summary_block


def generate_interview_summary(candidate_id, hr_scores, communication, behavior, answers):

    strengths = []
    weaknesses = []
    risks = []
    inconsistencies = []

    # -------------------------------
    # HR Analysis
    # -------------------------------
    for item in hr_scores:
        if item["final_score"] >= 80:
            strengths.append(f"Strong performance in {item['question_id']}")
        elif item["final_score"] < 50:
            weaknesses.append(f"Weak response in {item['question_id']}")

    # -------------------------------
    # Communication
    # -------------------------------
    if communication["communication_score"] >= 80:
        strengths.append("Excellent communication skills")
    elif communication["communication_score"] < 50:
        weaknesses.append("Poor communication clarity")

    # -------------------------------
    # Behavior
    # -------------------------------
    if behavior["confidence"]["confidence_score"] < 60:
        risks.append("Low confidence detected")

    if behavior.get("contradiction", False):
        inconsistencies.append("Contradictory statements observed")

    # -------------------------------
    # Cultural Fit
    # -------------------------------
    culture_fit = "Good" if "team" in str(answers).lower() else "Moderate"

    # -------------------------------
    # Scoring + Decision
    # -------------------------------
    overall_score = calculate_overall_score(hr_scores, communication, behavior)
    decision = get_decision(overall_score)

    # -------------------------------
    # FINAL RESULT
    # -------------------------------
    result = {
    "candidate_id": candidate_id,
    "overall_score": overall_score,
    "decision": decision,
    "final_recommendation": build_recommendation(decision,overall_score),

    "summary": {
        "strengths": strengths,
        "weaknesses": weaknesses,
        "risks": risks,
        "inconsistencies": inconsistencies,
        "cultural_fit": culture_fit
    },
    "natural_language_summary": generate_natural_summary(
        strengths, weaknesses, risks, culture_fit, decision
    )
}

    result["formatted_summary"] = format_summary_block(result["summary"])

    return result