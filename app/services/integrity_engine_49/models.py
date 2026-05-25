from pydantic import BaseModel


class IntegrityRequest(BaseModel):

    tab_switch: int
    focus_loss: int
    voice_detect: int
    gaze_off: int