import re
from datetime import datetime

MONTH_MAP = {
    "jan": 1, "feb": 2, "mar": 3, "apr": 4,
    "may": 5, "jun": 6, "jul": 7, "aug": 8,
    "sep": 9, "oct": 10, "nov": 11, "dec": 12
}


def parse_date(date_str):
    date_str = date_str.lower().strip()

    if "present" in date_str:
        return datetime.now()

    parts = date_str.split()
    if len(parts) == 2:
        month = MONTH_MAP.get(parts[0][:3], 1)
        year = int(parts[1])
        return datetime(year, month, 1)

    return None


def calculate_months(start, end):
    return (end.year - start.year) * 12 + (end.month - start.month)


def extract_experience(text):
    experiences = []
    total_months = 0

    # 🔥 Find ALL date ranges
    date_pattern = r"(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)?\s*\d{4}\s*-\s*(present|\d{4})"

    matches = re.finditer(date_pattern, text, re.IGNORECASE)

    for m in matches:
        date_range = m.group()

        parts = re.split(r"-", date_range)

        if len(parts) != 2:
            continue

        start = parse_date(parts[0].strip())
        end = parse_date(parts[1].strip())

        if start and end:
            duration = calculate_months(start, end)
            total_months += duration

            # 🔥 Extract nearby text as role/company
            span_start = max(0, m.start() - 50)
            span_end = m.end() + 50
            context = text[span_start:span_end]

            experiences.append({
                "company": "unknown",
                "role": context[:50],
                "start_date": start.strftime("%Y-%m"),
                "end_date": end.strftime("%Y-%m"),
                "duration_months": duration
            })

    return {
        "experiences": experiences,
        "total_experience_months": total_months
    }

def detect_gaps(experiences):
    gaps = []

    sorted_exp = sorted(experiences, key=lambda x: x["start_date"])

    for i in range(len(sorted_exp) - 1):
        end = datetime.strptime(sorted_exp[i]["end_date"], "%Y-%m")
        next_start = datetime.strptime(sorted_exp[i+1]["start_date"], "%Y-%m")

        diff = calculate_months(end, next_start)

        if diff > 1:
            gaps.append(f"{sorted_exp[i]['end_date']} to {sorted_exp[i+1]['start_date']}")

    return gaps


def detect_overlaps(experiences):
    overlaps = []

    for i in range(len(experiences)):
        for j in range(i + 1, len(experiences)):
            start1 = datetime.strptime(experiences[i]["start_date"], "%Y-%m")
            end1 = datetime.strptime(experiences[i]["end_date"], "%Y-%m")

            start2 = datetime.strptime(experiences[j]["start_date"], "%Y-%m")
            end2 = datetime.strptime(experiences[j]["end_date"], "%Y-%m")

            if start1 <= end2 and start2 <= end1:
                overlaps.append((experiences[i]["role"], experiences[j]["role"]))

    return overlaps