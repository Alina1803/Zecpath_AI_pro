# ----------------------------------------
# Browser Tab Switching Monitor
# ----------------------------------------

def detect_tab_switches(count):

    if count >= 5:
        return "High"

    elif count >= 2:
        return "Moderate"

    return "Low"