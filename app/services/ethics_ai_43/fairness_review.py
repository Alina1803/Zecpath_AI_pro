def remove_bias_features(candidate_data):
    # Remove demographic fields
    bias_fields = ["name", "gender", "age", "religion", "location"]
    return {k: v for k, v in candidate_data.items() if k not in bias_fields}


def fairness_score(scores):
    # Normalize fairness across candidates
    return sum(scores) / len(scores) if scores else 0