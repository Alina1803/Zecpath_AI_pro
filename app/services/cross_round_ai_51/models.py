from pydantic import BaseModel


class AggregationRequest(BaseModel):

    candidate_id: str

    role_type: str

    ats: float

    screening: float

    hr: float

    technical: float

    machine_test: float