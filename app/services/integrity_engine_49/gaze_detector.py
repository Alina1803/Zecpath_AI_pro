# ----------------------------------------
# Repeated Gaze Diversion Detection
# ----------------------------------------


def detect_gaze_deviation(count):

    if count >= 5:
        return "Frequent Gaze Diversion"

    elif count >= 2:
        return "Occasional Diversion"

    return "Stable Eye Contact"
