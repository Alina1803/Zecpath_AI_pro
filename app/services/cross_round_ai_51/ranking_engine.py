# -----------------------------------
# Candidate Ranking Engine
# -----------------------------------

def rank_candidate(score):

    if score >= 90:

        return {
            "rank": "A+",
            "category": "Elite Candidate"
        }

    elif score >= 80:

        return {
            "rank": "A",
            "category": "Strong Candidate"
        }

    elif score >= 70:

        return {
            "rank": "B",
            "category": "Good Candidate"
        }

    elif score >= 60:

        return {
            "rank": "C",
            "category": "Average Candidate"
        }

    return {
        "rank": "D",
        "category": "Low Candidate"
    }