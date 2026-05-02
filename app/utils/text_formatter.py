"""
Text Formatter Utilities
------------------------
Used for formatting outputs in summary generation.
Ensures consistency across reports.
"""


# ===============================
# 🔤 FORMAT LIST TO STRING
# ===============================
def format_list(items, default="None"):
    """
    Convert list to readable string
    """
    if not items:
        return default
    return ", ".join(items)


# ===============================
# ✨ CAPITALIZE SENTENCES
# ===============================
def capitalize_text(text: str) -> str:
    """
    Capitalize first letter of each sentence
    """
    if not text:
        return ""

    sentences = text.split(". ")
    sentences = [s.capitalize() for s in sentences]

    return ". ".join(sentences)


# ===============================
# 📌 BULLET FORMAT
# ===============================
def to_bullets(items):
    """
    Convert list to bullet points
    """
    if not items:
        return "- None"

    return "\n".join([f"- {item}" for item in items])


# ===============================
# 🎯 HIGHLIGHT TEXT
# ===============================
def highlight(text: str) -> str:
    """
    Highlight important text (for logs/UI)
    """
    return f"*** {text.upper()} ***"


# ===============================
# 🧾 FORMAT SUMMARY BLOCK
# ===============================
def format_summary_block(summary: dict) -> str:
    """
    Convert structured summary into readable block
    """

    strengths = to_bullets(summary.get("strengths", []))
    weaknesses = to_bullets(summary.get("weaknesses", []))
    risks = to_bullets(summary.get("risks", []))
    inconsistencies = to_bullets(summary.get("inconsistencies", []))
    culture = summary.get("cultural_fit", "Unknown")

    return f"""
=== Candidate Summary ===

Strengths:
{strengths}

Weaknesses:
{weaknesses}

Risks:
{risks}

Inconsistencies:
{inconsistencies}

Cultural Fit: {culture}
"""
    

# ===============================
# 🧪 DEBUG FORMATTER
# ===============================
if __name__ == "__main__":
    sample = {
        "strengths": ["Good communication", "Team player"],
        "weaknesses": ["Low confidence"],
        "risks": [],
        "inconsistencies": [],
        "cultural_fit": "Good"
    }

    print(format_summary_block(sample))