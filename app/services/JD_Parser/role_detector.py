import re
from app.services.JD_Parser.ca_roles import CA_ROLES


def detect_roles(text: str, roles):
    text = text.lower()
    detected_roles = []

    for role in roles:
        role_lower = role.lower()
        matched_keywords = []

        if role_lower in text:
            matched_keywords.append(role_lower)

        if matched_keywords:
            detected_roles.append({
                "role": role,
                "matched_keywords": matched_keywords,
                "confidence": 100.0
            })

    return detected_roles