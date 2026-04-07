def rank_candidates(candidates):
    """
    Sort candidates by final_score descending
    and assign rank positions.
    """
    ranked = sorted(
        candidates,
        key=lambda x: x["scores"]["final_score"],
        reverse=True
    )

    for index, candidate in enumerate(ranked, start=1):
        candidate["rank"] = index

    return ranked