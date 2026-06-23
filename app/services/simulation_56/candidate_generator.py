import random
import uuid

ROLES = [
    "Backend Developer",
    "Frontend Developer",
    "DevOps Engineer",
    "Data Engineer",
    "AI Engineer",
]

LEVELS = ["Fresher", "Junior", "Mid", "Senior"]


def generate_candidate():

    profile = random.choice(
        ["strong_ats", "strong_technical", "strong_hr", "balanced", "high_risk"]
    )

    candidate = {
        "candidate_id": str(uuid.uuid4()),
        "role": random.choice(ROLES),
        "experience_level": random.choice(LEVELS),
        "profile_type": profile,
    }

    return candidate


def generate_candidates(count=50):
    return [generate_candidate() for _ in range(count)]
