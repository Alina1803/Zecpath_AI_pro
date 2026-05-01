from app.models.ideal_patterns38 import get_keywords

def evaluate_scenario(text, scenario_type):
    """
    Evaluate answer against ideal behavioral patterns
    """

    text = text.lower()
    keywords = get_keywords(scenario_type)

    if not keywords:
        return None  # unknown scenario

    match_count = sum(word in text for word in keywords)

    if match_count == len(keywords):
        return 1.0
    elif match_count > 0:
        return 0.7
    return 0.4