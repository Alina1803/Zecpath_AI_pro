import os
import re
import json
from PyPDF2 import PdfReader


def extract_roles_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""

    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text() + "\n"

    # Extract roles like "1. Audit Manager"
    matches = re.findall(r'\n?\d+\.\s+([A-Za-z &()/\-]+)', text)

    roles = []
    for role in matches:
        role = role.lower().strip()
        role = role.replace("(ca)", "").strip()

        # remove noise
        if len(role) < 3:
            continue
        if "role summary" in role:
            continue

        roles.append(role)

    roles = sorted(list(set(roles)))

    return roles


def save_roles(roles, path="data/processed/output_6_jd/roles.json"):
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w") as f:
        json.dump(roles, f, indent=4)