import uuid


def generate_candidate_id() -> str:
    return f"CAND_{uuid.uuid4().hex[:8]}"


def generate_job_id() -> str:
    return f"JOB_{uuid.uuid4().hex[:6]}"


def normalize_text(text: str) -> str:
    return text.strip().lower()

def clean_input(text: str):
    return text.strip()

def preprocess_input(data: list):
    return data