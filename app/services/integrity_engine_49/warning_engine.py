# ----------------------------------------
# Real-Time Warning Generator
# ----------------------------------------

def generate_warning(events):

    warnings = []

    if events["tab_switch"] > 2:

        warnings.append(
            "Please stay on the interview screen"
        )

    if events["voice_detect"] > 1:

        warnings.append(
            "External voice detected. Please ensure privacy"
        )

    if events["focus_loss"] > 3:

        warnings.append(
            "Focus loss detected during interview"
        )

    return warnings