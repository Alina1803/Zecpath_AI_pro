# ----------------------------------------
# Integrity Score Calculation
# ----------------------------------------

def calculate_integrity_score(events):

    score = 100

    score -= events["tab_switch"] * 5

    score -= events["focus_loss"] * 4

    score -= events["voice_detect"] * 10

    score -= events["gaze_off"] * 3

    return max(score, 0)