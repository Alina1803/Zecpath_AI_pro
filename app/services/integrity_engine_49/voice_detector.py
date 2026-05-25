# ----------------------------------------
# External Voice Detection
# ----------------------------------------

def analyze_external_voice(count):

    if count >= 3:
        return "External Assistance Suspected"

    elif count >= 1:
        return "Background Voice Detected"

    return "No External Voice"