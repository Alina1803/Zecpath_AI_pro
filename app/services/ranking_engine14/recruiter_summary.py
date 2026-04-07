def generate_summary(candidates):
    """
    Generate recruiter-friendly hiring summary.
    """
    shortlisted = sum(
        1 for c in candidates if c["decision"] == "SHORTLIST"
    )

    review = sum(
        1 for c in candidates if c["decision"] == "REVIEW"
    )

    rejected = sum(
        1 for c in candidates if c["decision"] == "REJECT"
    )

    return {
        "total_candidates": len(candidates),
        "shortlisted": shortlisted,
        "review": review,
        "rejected": rejected
    }