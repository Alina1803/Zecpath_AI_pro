import json

# ------------------------
# Decision Engine
# ------------------------


def decision(score):

    if score >= 75:
        return "Selected"

    elif score >= 55:
        return "Hold / Review"

    return "Rejected"


# ------------------------
# Candidate Simulation
# ------------------------


def simulate(candidate):

    final_score = round(
        (
            candidate["ats_score"]
            + candidate["screening_score"]
            + candidate["interview_score"]
        )
        / 3
    )

    return {
        "candidate_id": candidate["candidate_id"],
        "final_score": final_score,
        "decision": decision(final_score),
    }


# ------------------------
# Demo Dataset
# ------------------------

demo_candidates = [
    {
        "candidate_id": "C001",
        "ats_score": 85,
        "screening_score": 80,
        "interview_score": 88,
    },
    {
        "candidate_id": "C002",
        "ats_score": 65,
        "screening_score": 68,
        "interview_score": 72,
    },
    {
        "candidate_id": "C003",
        "ats_score": 40,
        "screening_score": 50,
        "interview_score": 45,
    },
]


# ------------------------
# Run Pipeline
# ------------------------


def run_pipeline():

    output = []

    for candidate in demo_candidates:

        output.append(simulate(candidate))

    return output


# ------------------------
# Execute
# ------------------------

if __name__ == "__main__":

    result = run_pipeline()

    print(json.dumps(result, indent=4))
