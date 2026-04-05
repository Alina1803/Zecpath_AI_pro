from app.services.experience_engine.similarity_engine import compute_similarity


def experience_relevance(experience_data, job_description):
    experiences = experience_data["experiences"]

    total_score = 0
    detailed_scores = []

    for exp in experiences:
        role_text = exp["role"]

        score = compute_similarity(role_text, job_description)

        weighted_score = score * exp["duration_months"]

        total_score += weighted_score

        detailed_scores.append({
            "role": role_text,
            "company": exp["company"],
            "score": round(score * 100, 2)
        })

    total_exp = experience_data["total_experience_months"]

    if total_exp == 0:
        return {"relevance_score": 0, "details": []}

    final_score = (total_score / total_exp) * 100

    return {
        "relevance_score": round(final_score, 2),
        "details": detailed_scores
    }