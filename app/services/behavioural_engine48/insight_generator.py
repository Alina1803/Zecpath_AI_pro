# -----------------------------------
# Insight Generator
# -----------------------------------

def generate_behavior_insights(score):

    if score >= 85:

        return {
            "focus_level": "Highly Focused",
            "engagement": "Excellent",
            "risk": "Low"
        }

    elif score >= 70:

        return {
            "focus_level": "Good",
            "engagement": "Strong",
            "risk": "Low"
        }

    elif score >= 50:

        return {
            "focus_level": "Moderate",
            "engagement": "Average",
            "risk": "Moderate"
        }

    return {
        "focus_level": "Distracted",
        "engagement": "Low",
        "risk": "High"
    }