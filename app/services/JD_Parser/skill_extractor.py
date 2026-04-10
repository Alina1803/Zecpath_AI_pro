import re
from typing import List, Dict

# -------------------------------
# Predefined Skill Dictionaries
# -------------------------------

TECH_SKILLS = {
        "tally",
    "sap fico",
    "oracle financials",
    "quickbooks",
    "zoho books",
    "excel",
    "advanced excel",
    "power bi",
    "tableau",
    "sql",
    "erp systems",
    "ms office",
    "google sheets",
    "automation tools",
    "data analysis tools"

}

ACCOUNTING_SKILLS = {
    "gst","taxation","tds","income tax","corporate tax",
    "audit","statutory audit","internal audit","forensic audit",
    "financial reporting","ifrs","gaap","accounts payable",
    "accounts receivable","bank reconciliation","general ledger",
    "finalization of accounts","cost accounting","variance analysis",
    "budgeting","forecasting","cash flow management","financial analysis",
    "compliance","roc filing","transfer pricing"
}

SOFT_SKILLS = {
    "communication",
    "analytical thinking",
    "problem solving",
    "attention to detail",
    "time management",
    "leadership",
    "team management",
    "decision making",
    "critical thinking",
    "adaptability",
    "client handling",
    "presentation skills",
    "negotiation",
    "organizational skills"
}

# Combine all skills
ALL_SKILLS = TECH_SKILLS | ACCOUNTING_SKILLS | SOFT_SKILLS


# -------------------------------
# Text Cleaner
# -------------------------------

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s+.#]', ' ', text)
    return text


# -------------------------------
# Skill Extraction Logic
# -------------------------------

def extract_skills(text: str) -> Dict[str, List[str]]:
    cleaned = clean_text(text)

    found_skills = set()

    for skill in ALL_SKILLS:
        # exact word / phrase match
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, cleaned):
            found_skills.add(skill)

    # Categorize
    categorized = {
        "technical_skills": [],
        "accounting_skills": [],
        "soft_skills": []
    }

    for skill in found_skills:
        if skill in TECH_SKILLS:
            categorized["technical_skills"].append(skill)
        elif skill in ACCOUNTING_SKILLS:
            categorized["accounting_skills"].append(skill)
        elif skill in SOFT_SKILLS:
            categorized["soft_skills"].append(skill)

    # Sort for consistency
    for key in categorized:
        categorized[key] = sorted(categorized[key])

    return categorized


# -------------------------------
# Skill Matching (Resume vs JD)
# -------------------------------

def match_skills(resume_skills: Dict, jd_skills: Dict) -> Dict:
    result = {}

    for category in resume_skills:
        res_set = set(resume_skills.get(category, []))
        jd_set = set(jd_skills.get(category, []))

        matched = res_set & jd_set
        missing = jd_set - res_set

        result[category] = {
            "matched": list(matched),
            "missing": list(missing),
            "match_percentage": round(
                (len(matched) / len(jd_set)) * 100, 2
            ) if jd_set else 0
        }

    return result