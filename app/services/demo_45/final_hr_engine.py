from app.services.demo_45.scoring_engine import calculate_scores
from app.services.demo_45.summary_engine import generate_summary


def run_hr_interview(candidate_id, answers):
    """
    Main HR Interview AI Pipeline

    Steps:
    1. Process answers
    2. Calculate scores
    3. Generate summary
    4. Make hiring decision
    """

    # -----------------------------------
    # Calculate Scores
    # -----------------------------------
    scores = calculate_scores(answers)

    # -----------------------------------
    # Unified Final Score
    # -----------------------------------
    final_score = (
        scores["ats"] * 0.3 +
        scores["screening"] * 0.3 +
        scores["hr"] * 0.4
    )

    final_score = round(final_score, 2)

    # -----------------------------------
    # Hiring Decision
    # -----------------------------------
    if final_score >= 75:
        decision = "Hire"
    elif final_score >= 60:
        decision = "Hold"
    else:
        decision = "Reject"

    # -----------------------------------
    # Generate Summary
    # -----------------------------------
    summary = generate_summary(scores)

    # -----------------------------------
    # Final Result
    # -----------------------------------
    result = {
        "candidate_id": candidate_id,
        "scores": scores,
        "final_score": final_score,
        "decision": decision,
        "summary": summary
    }

    return result