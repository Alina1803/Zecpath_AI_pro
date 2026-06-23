# -----------------------------------
# Head Stability Analysis
# -----------------------------------


def analyze_head_movement(stability):

    if stability > 0.8:
        return "Stable"

    elif stability > 0.5:
        return "Slight Movement"

    return "Frequent Movement"
