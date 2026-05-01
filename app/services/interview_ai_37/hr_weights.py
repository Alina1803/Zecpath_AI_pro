"""
Weight Configuration System
"""

ROLE_WEIGHTS = {
    "fresher": {
        "relevance": 0.25,
        "communication": 0.30,
        "confidence": 0.25,
        "consistency": 0.20
    },
    "experienced": {
        "relevance": 0.35,
        "communication": 0.20,
        "confidence": 0.25,
        "consistency": 0.20
    }
}


def get_weights(candidate_type):
    return ROLE_WEIGHTS.get(candidate_type, ROLE_WEIGHTS["fresher"])