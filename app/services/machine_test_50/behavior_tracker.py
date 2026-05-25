# --------------------------------------
# Candidate Behavior Tracking
# --------------------------------------

def behavior_analysis(edit_count):

    if edit_count > 30:
        return "Highly Iterative"

    elif edit_count > 10:
        return "Moderate Activity"

    return "Low Editing Activity"