from datetime import datetime

def months_between(start, end):

    start_date = datetime.strptime(start, "%b %Y")

    # handle Present / Current
    if end.lower() in ["present", "current", "now"]:
        end_date = datetime.now()
    else:
        end_date = datetime.strptime(end, "%b %Y")

    months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)

    return months

def calculate_total_experience(experiences):

    total_months = 0

    for role in experiences:

        duration = months_between(role["start"], role["end"])

        role["duration_months"] = duration

        total_months += duration

    return round(total_months / 12, 2)

def detect_gaps_and_overlaps(experiences):

    gaps = []
    overlaps = []

    durations = [e.get("duration_months", 0) for e in experiences]

    if not durations:
        return gaps, overlaps

    for i in range(len(durations) - 1):

        if durations[i] == 0:
            gaps.append(i)

        if durations[i] < durations[i + 1]:
            overlaps.append((i, i + 1))

    return gaps, overlaps


def relevance_score(experiences, target_role):
    score = 0
    for exp in experiences:
        if "cyber" in target_role.lower():
            score += 10
    return min(score, 100)