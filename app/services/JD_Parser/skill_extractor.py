import re
from typing import List, Dict

# -------------------------------
# Predefined Skill Dictionaries
# -------------------------------

TECH_SKILLS = {
    "python","java","sql","fastapi","machine learning",
    "backend development","api development",
    "tally", "sap fico", "oracle financials", "quickbooks",
    "zoho books", "excel", "advanced excel", "power bi",
    "tableau", "sql", "erp systems", "ms office",
    "google sheets", "automation tools", "data analysis tools"
}

ACCOUNTING_SKILLS = {
    "gst", "taxation", "tds", "income tax", "corporate tax",
    "audit", "statutory audit", "internal audit", "forensic audit",
    "financial reporting", "ifrs", "gaap", "accounts payable",
    "accounts receivable", "bank reconciliation", "general ledger",
    "finalization of accounts", "cost accounting", "variance analysis",
    "budgeting", "forecasting", "cash flow management", "financial analysis",
    "compliance", "roc filing", "transfer pricing"
}

SOFT_SKILLS = {
    "communication", "analytical thinking", "problem solving",
    "attention to detail", "time management", "leadership",
    "team management", "decision making", "critical thinking",
    "adaptability", "client handling", "presentation skills",
    "negotiation", "organizational skills"
}

ALL_SKILLS = TECH_SKILLS | ACCOUNTING_SKILLS | SOFT_SKILLS


# -------------------------------
# Text Cleaner (IMPROVED)
# -------------------------------
def clean_text(text: str) -> str:
    if not text:
        return ""

    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s+.#]', ' ', text)
    text = re.sub(r'\s+', ' ', text)  # remove extra spaces
    return text.strip()


# -------------------------------
# Skill Extraction (ROBUST)
# -------------------------------
def extract_skills(text: str) -> Dict[str, List[str]]:
    
    # 🔒 Safety check
    if not text or not isinstance(text, str):
        return {
            "technical_skills": [],
            "accounting_skills": [],
            "soft_skills": []
        }

    cleaned = clean_text(text)

    categorized = {
        "technical_skills": [],
        "accounting_skills": [],
        "soft_skills": []
    }

    # 🔍 Skill matching
    for skill in ALL_SKILLS:
        pattern = r'\b' + re.escape(skill) + r'\b'

        if re.search(pattern, cleaned):
            if skill in TECH_SKILLS:
                categorized["technical_skills"].append(skill)

            elif skill in ACCOUNTING_SKILLS:
                categorized["accounting_skills"].append(skill)

            elif skill in SOFT_SKILLS:
                categorized["soft_skills"].append(skill)

    # ✅ Remove duplicates + sort
    for key in categorized:
        categorized[key] = sorted(set(categorized[key]))

    # 🧠 DEBUG (keep temporarily)
    print("🧠 Extracted Skills:", categorized)

    return categorized


# -------------------------------
# Skill Matching (ATS LEVEL)
# -------------------------------
def match_skills(resume_skills: Dict, jd_skills: Dict) -> Dict:

    result = {}
    total_matched = 0
    total_required = 0

    # Ensure all categories exist
    categories = ["technical_skills", "accounting_skills", "soft_skills"]

    for category in categories:
        res_set = set(resume_skills.get(category, []))
        jd_set = set(jd_skills.get(category, []))

        matched = res_set & jd_set
        missing = jd_set - res_set

        match_percentage = (
            (len(matched) / len(jd_set)) * 100
            if jd_set else 0
        )

        result[category] = {
            "matched": sorted(list(matched)),
            "missing": sorted(list(missing)),
            "match_percentage": round(match_percentage, 2)
        }

        total_matched += len(matched)
        total_required += len(jd_set)

    # -------------------------------
    # OVERALL SCORE
    # -------------------------------
    overall_score = (
        (total_matched / total_required) * 100
        if total_required else 0
    )

    result["overall"] = {
        "matched_count": total_matched,
        "required_count": total_required,
        "overall_match_percentage": round(overall_score, 2)
    }

    # -------------------------------
    # SHORTLIST DECISION
    # -------------------------------
    result["decision"] = (
        "shortlisted" if overall_score >= 60 else "rejected"
    )

    return result