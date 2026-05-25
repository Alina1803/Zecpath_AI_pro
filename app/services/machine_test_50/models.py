from pydantic import BaseModel


class MachineTestRequest(BaseModel):

    candidate_id: str

    task_id: str

    passed: int

    total: int

    runtime: float

    code_snapshot: str

    attempts: int

    time_taken: int