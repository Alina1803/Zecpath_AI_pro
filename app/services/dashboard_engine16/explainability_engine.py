def explain_candidate(candidate):
    scores = candidate["scores"]

    return {
        "final_score": scores["final_score"],
        "normalized_score": scores.get("normalized_score", 0),
        "explanation": (
            "Candidate ranked based on ATS, experience, "
            "education, and semantic relevance."
        )
    }