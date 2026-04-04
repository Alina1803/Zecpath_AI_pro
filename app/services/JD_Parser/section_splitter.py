import re
from typing import List, Dict


# =====================================================
# 1) SPLIT FULL PDF INTO ROLE BLOCKS
# =====================================================
def split_role_blocks(text: str) -> List[Dict]:
    """
    Split full CA domain PDF into numbered role blocks.
    Example:
    1. Chartered Accountant
    2. Banking Accountant
    """
    text = text.replace("\r", "\n")

    # Split at numbered headings
    pattern = r'(?=\n?\d+\.\s+[A-Za-z])'
    chunks = re.split(pattern, text)

    role_blocks = []

    for chunk in chunks:
        chunk = chunk.strip()
        if not chunk:
            continue

        first_line = chunk.split("\n")[0]

        match = re.match(r'(\d+)\.\s+(.+)', first_line)
        if not match:
            continue

        role_number = match.group(1)
        role_name = match.group(2).strip()

        role_blocks.append({
            "role_number": role_number,
            "role_name": role_name,
            "text": chunk
        })

    return role_blocks


# =====================================================
# 2) SPLIT SINGLE ROLE INTO JD SECTIONS
# =====================================================
def split_sections(text: str) -> Dict[str, str]:
    """
    Robust section splitter for inline PDF extracted text.
    Works even when headers are in same line.
    """
    sections = {
        "role_summary": "",
        "responsibilities": "",
        "qualifications": ""
    }

    text = text.replace("\r", "\n")

    summary_match = re.search(
        r'role summary[:\s]*(.*?)(?=key responsibilities[:\s]|skills\s*&\s*qualifications[:\s]|$)',
        text,
        re.IGNORECASE | re.DOTALL
    )

    responsibilities_match = re.search(
        r'key responsibilities[:\s]*(.*?)(?=skills\s*&\s*qualifications[:\s]|$)',
        text,
        re.IGNORECASE | re.DOTALL
    )

    qualifications_match = re.search(
        r'skills\s*&\s*qualifications[:\s]*(.*?)(?=career scope[:\s]|business scope[:\s]|$)',
        text,
        re.IGNORECASE | re.DOTALL
    )

    if summary_match:
        sections["role_summary"] = summary_match.group(1).strip()

    if responsibilities_match:
        sections["responsibilities"] = responsibilities_match.group(1).strip()

    if qualifications_match:
        sections["qualifications"] = qualifications_match.group(1).strip()

    return sections