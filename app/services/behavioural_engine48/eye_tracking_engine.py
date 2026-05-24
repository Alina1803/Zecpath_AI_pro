# -----------------------------------
# Eye Tracking Analysis
# -----------------------------------

def analyze_eye_focus(gaze_stability):

    if gaze_stability > 0.8:
        return "High Focus"

    elif gaze_stability > 0.5:
        return "Moderate Focus"

    return "Low Focus"