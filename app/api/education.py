from fastapi import APIRouter
from pydantic import BaseModel

from utils import text_cleaner
from app.services.education_engine.education_parser import parse_education
from app.services.education_engine.certification_parser import extract_certifications
from app.services.education_engine.relevance_engine import certification_relevance


router = APIRouter()

class ResumeInput(BaseModel):
    text: str


@router.post("/parse-education")
def parse_resume_education(data: ResumeInput):
    text = data.text

    education = parse_education(text)
    certifications = extract_certifications(text)

    cert_output = []
    for cert in certifications:
        cert_output.append({
            "name": cert,
            "category": certification_relevance(cert)
        })

    return {
        "education": education,
        "certifications": cert_output
    }