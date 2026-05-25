# ----------------------------------------
# Event Aggregation Engine
# ----------------------------------------

def aggregate_events(data):

    return {
        "tab_switch": data.tab_switch,
        "focus_loss": data.focus_loss,
        "voice_detect": data.voice_detect,
        "gaze_off": data.gaze_off
    }