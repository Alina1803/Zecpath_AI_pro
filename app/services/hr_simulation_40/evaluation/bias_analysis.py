def analyze_bias(results):
    bias = {}

    for r in results:
        t = r["type"]
        diff = r["ai_score"] - r["human_score"]

        if t not in bias:
            bias[t] = []

        bias[t].append(diff)

    return {k: sum(v)/len(v) for k, v in bias.items()}