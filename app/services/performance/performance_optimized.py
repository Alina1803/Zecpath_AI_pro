from functools import lru_cache

# -------------------------
# ATS Cache
# -------------------------


@lru_cache(maxsize=1000)
def cached_ats_score(profile_hash):

    return hash(profile_hash) % 100


# -------------------------
# Batch Processing
# -------------------------


def batch_resume_processing(
    resume_list,
    process_func,
):

    results = []

    for resume in resume_list:

        results.append(process_func(resume))

    return results


# -------------------------
# Fast Decision Engine
# -------------------------


def fast_decision(score):

    if score >= 75:

        return "Selected"

    elif score >= 55:

        return "Review"

    return "Rejected"
