def normalize_candidate(candidate):
    """
    Normalize candidate structure into standard format.
    """
    return {
        "file_name": candidate.get("file_name", ""),
        "skills": candidate.get("skills", []),
        "experience": candidate.get("experience", []),
        "education": candidate.get("education", []),
        "certifications": candidate.get("certifications", []),
        "scores": candidate.get("scores", {}),
        "rank": candidate.get("rank", None),
        "decision": candidate.get("decision", None)
    }