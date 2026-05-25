# ----------------------------------------
# Behavioral Pattern Recognition
# ----------------------------------------

def detect_patterns(events):

    patterns = []

    if events["tab_switch"] >= 3:
        patterns.append("Possible Browser Searching")

    if events["voice_detect"] >= 2:
        patterns.append("Possible External Assistance")

    if (
        events["gaze_off"] >= 4 and
        events["focus_loss"] >= 3
    ):
        patterns.append("Possible Note Referencing")

    return patterns