# -----------------------------------
# Benchmark Intelligence
# -----------------------------------


def benchmark_score(score):

    if score >= 90:
        return "Top 5%"

    elif score >= 80:
        return "Top 15%"

    elif score >= 70:
        return "Top 30%"

    return "Average Pool"
