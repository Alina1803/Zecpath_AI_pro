from pydantic import BaseModel


class BehaviorRequest(BaseModel):

    eye_focus: float
    head_stability: float
    engagement: float
    distraction: float
