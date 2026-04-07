from datetime import datetime
import re


# ==============================
# 🎯 MONTH MAPPING
# ==============================

MONTH_MAP = {
    "jan": "01", "january": "01",
    "feb": "02", "february": "02",
    "mar": "03", "march": "03",
    "apr": "04", "april": "04",
    "may": "05",
    "jun": "06", "june": "06",
    "jul": "07", "july": "07",
    "aug": "08", "august": "08",
    "sep": "09", "september": "09",
    "oct": "10", "october": "10",
    "nov": "11", "november": "11",
    "dec": "12", "december": "12"
}


# ==============================
# 🎯 CLEAN DATE STRING
# ==============================

def normalize_date(date_str: str):
    """
    Convert date like:
    'Jan 2020' → '2020-01'
    'March 2021' → '2021-03'
    '2022' → '2022-01'
    'Present' → current date
    """

    if not date_str:
        return None

    date_str = date_str.strip().lower()

    # Handle "Present"
    if "present" in date_str or "current" in date_str:
        return datetime.now().strftime("%Y-%m")

    # Extract year
    year_match = re.search(r"\b(19|20)\d{2}\b", date_str)
    year = year_match.group() if year_match else None

    # Extract month
    month = "01"  # default

    for key in MONTH_MAP:
        if key in date_str:
            month = MONTH_MAP[key]
            break

    if year:
        return f"{year}-{month}"

    return None


# ==============================
# 🎯 MONTH DIFFERENCE
# ==============================

def calculate_months(start_date: str, end_date: str):
    """
    Calculate months between two dates (YYYY-MM)
    """

    if not start_date or not end_date:
        return 0

    try:
        start = datetime.strptime(start_date, "%Y-%m")
        end = datetime.strptime(end_date, "%Y-%m")

        return (end.year - start.year) * 12 + (end.month - start.month)

    except Exception:
        return 0


# ==============================
# 🎯 TOTAL EXPERIENCE
# ==============================

def calculate_total_experience(experiences):
    """
    experiences = [
        {
            "start_date": "2020-01",
            "end_date": "2022-03"
        }
    ]
    """

    total_months = 0

    for exp in experiences:
        start = exp.get("start_date")
        end = exp.get("end_date")

        total_months += calculate_months(start, end)

    return total_months


# ==============================
# 🎯 FORMAT MONTHS → YEARS
# ==============================

def format_experience(months):
    """
    Convert months → 'X years Y months'
    """

    years = months // 12
    remaining_months = months % 12

    return f"{years} years {remaining_months} months"