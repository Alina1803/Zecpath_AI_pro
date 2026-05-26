# -----------------------------------
# Default Weight Distribution
# -----------------------------------

DEFAULT_WEIGHTS = {

    "ats": 0.20,

    "screening": 0.15,

    "hr": 0.20,

    "technical": 0.25,

    "machine_test": 0.20
}


# -----------------------------------
# Role-Based Weight Configuration
# -----------------------------------

ROLE_WEIGHTS = {

    "technical": {

        "ats": 0.15,

        "screening": 0.10,

        "hr": 0.15,

        "technical": 0.35,

        "machine_test": 0.25
    },

    "non_technical": {

        "ats": 0.25,

        "screening": 0.20,

        "hr": 0.35,

        "technical": 0.10,

        "machine_test": 0.10
    },

    "fresher": {

        "ats": 0.20,

        "screening": 0.20,

        "hr": 0.25,

        "technical": 0.20,

        "machine_test": 0.15
    }
}


def get_weights(role_type):

    return ROLE_WEIGHTS.get(
        role_type,
        DEFAULT_WEIGHTS
    )


# -----------------------------------
# Final Aggregated Score
# -----------------------------------

def calculate_final_score(scores, weights):

    final = 0

    for key in weights:

        final += scores.get(key, 0) * weights[key]

    return round(final, 2)