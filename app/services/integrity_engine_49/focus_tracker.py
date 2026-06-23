def detect_focus_loss(count):

    if count >= 6:
        return "Severe Focus Loss"

    elif count >= 3:
        return "Moderate Focus Loss"

    return "Stable Attention"
