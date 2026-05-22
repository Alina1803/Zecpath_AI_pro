from app.services.summary_39.decision_engine import (
    calculate_overall_score,
    get_decision,
    build_recommendation
)

from app.services.summary_39.summary_templates import (
    generate_natural_summary
)

from app.utils.text_formatter import (
    format_summary_block
)


def generate_interview_summary(

    candidate_id="UNKNOWN",

    hr_scores=None,

    communication=None,

    behavior=None,

    answers=None,

    # ==========================================
    # NEW SAFE OPTIONAL PARAMETERS
    # ==========================================

    role=None,

    experience=None,

    responses=None,

    overall_score=None,

    **kwargs
):

    # ==========================================
    # SAFE DEFAULTS
    # ==========================================

    hr_scores = hr_scores or []

    communication = communication or {}

    behavior = behavior or {}

    answers = answers or []

    responses = responses or []

    strengths = []

    weaknesses = []

    risks = []

    inconsistencies = []

    # ==========================================
    # USE RESPONSES IF hr_scores EMPTY
    # ==========================================

    if not hr_scores and responses:

        hr_scores = responses

    # ==========================================
    # HR ANALYSIS
    # ==========================================

    for item in hr_scores:

        score = item.get("final_score", 0)

        qid = item.get(
            "question_id",
            item.get("question", "Unknown Question")
        )

        if score >= 80 or score >= 8:

            strengths.append(
                f"Strong performance in {qid}"
            )

        elif score < 50 or score < 5:

            weaknesses.append(
                f"Weak response in {qid}"
            )

    # ==========================================
    # COMMUNICATION ANALYSIS
    # ==========================================

    comm_score = 0

    if isinstance(communication, dict):

        comm_score = communication.get(
            "communication_score",
            communication.get(
                "final_score",
                0
            )
        )

    if comm_score >= 80:

        strengths.append(
            "Excellent communication skills"
        )

    elif comm_score < 50:

        weaknesses.append(
            "Poor communication clarity"
        )

    # ==========================================
    # BEHAVIOR ANALYSIS
    # ==========================================

    confidence_score = 0

    if isinstance(behavior, dict):

        confidence_score = behavior.get(
            "confidence",
            behavior.get(
                "confidence_score",
                0
            )
        )

    if confidence_score < 60:

        risks.append(
            "Low confidence detected"
        )

    contradiction = behavior.get(
        "contradiction",
        False
    )

    if contradiction:

        inconsistencies.append(
            "Contradictory statements observed"
        )

    # ==========================================
    # CULTURAL FIT
    # ==========================================

    combined_answers = str(answers) + str(responses)

    culture_fit = (

        "Good"

        if "team" in combined_answers.lower()

        else "Moderate"
    )

    # ==========================================
    # OVERALL SCORE
    # ==========================================

    if overall_score is None:

        try:

            overall_score = calculate_overall_score(
                hr_scores,
                communication,
                behavior
            )

        except Exception:

            total = sum(
                item.get("final_score", 0)
                for item in hr_scores
            )

            overall_score = (

                round(
                    total / len(hr_scores),
                    2
                )

                if hr_scores else 0
            )

    # ==========================================
    # DECISION
    # ==========================================

    decision = get_decision(
        overall_score
    )

    # ==========================================
    # FINAL RESULT
    # ==========================================

    result = {

        "candidate_id": candidate_id,

        "role": role,

        "experience": experience,

        "overall_score": overall_score,

        "decision": decision,

        "final_recommendation":

            build_recommendation(
                decision,
                overall_score
            ),

        "summary": {

            "strengths": strengths,

            "weaknesses": weaknesses,

            "risks": risks,

            "inconsistencies":
                inconsistencies,

            "cultural_fit":
                culture_fit
        },

        "natural_language_summary":

            generate_natural_summary(

                strengths,

                weaknesses,

                risks,

                culture_fit,

                decision
            )
    }

    result["formatted_summary"] = (

        format_summary_block(
            result["summary"]
        )
    )

    return result