from pydantic import BaseModel


class ResumeResponse(BaseModel):
    id: int
    summary: str | None = None
    skills: str | None = None
    experience: str | None = None
    education: str | None = None
    projects: str | None = None
    certifications: str | None = None

    class Config:
        from_attributes = True