def education_relevance(education, job_description):
    score = 0
    jd = job_description.lower()

    for edu in education:
        degree = edu.get("degree", "").lower()

        if "ca" in degree or "chartered accountant" in degree:
            if "accountant" in jd or "audit" in jd:
                score += 50

        if "mba" in degree:
            if "finance" in jd:
                score += 30

    return {
        "education_score": min(score, 100)
    }