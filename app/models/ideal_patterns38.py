"""
Ideal Answer Patterns for Scenario Evaluation
--------------------------------------------
Defines expected behavioral patterns for different HR scenarios.
Used by scenario_evaluator.py
"""


# ===============================
# 🎯 IDEAL PATTERN DEFINITIONS
# ===============================
IDEAL_PATTERNS = {
    "team_conflict": {
        "keywords": ["communicate", "understand", "resolve"],
        "description": "Candidate should focus on communication and resolution"
    },

    "deadline_pressure": {
        "keywords": ["prioritize", "plan", "execute"],
        "description": "Candidate should show time management and execution"
    },

    "learning": {
        "keywords": ["research", "practice", "apply"],
        "description": "Candidate should demonstrate learning process"
    },

    "decision_making": {
        "keywords": ["analyze", "consider", "decide"],
        "description": "Candidate should evaluate options before decision"
    },

    "problem_solving": {
        "keywords": ["identify", "analyze", "solve"],
        "description": "Candidate should follow structured problem solving"
    }
}


# ===============================
# 📥 GET PATTERN
# ===============================
def get_pattern(scenario_type: str):
    """
    Retrieve pattern config for given scenario
    """
    return IDEAL_PATTERNS.get(scenario_type, None)


# ===============================
# 📋 GET KEYWORDS ONLY
# ===============================
def get_keywords(scenario_type: str):
    """
    Get only keywords for a scenario
    """
    pattern = get_pattern(scenario_type)

    if pattern:
        return pattern["keywords"]

    return []


# ===============================
# 📚 LIST ALL SCENARIOS
# ===============================
def list_scenarios():
    """
    Return all available scenario types
    """
    return list(IDEAL_PATTERNS.keys())


# ===============================
# 🧪 DEBUG / TEST
# ===============================
if __name__ == "__main__":
    print("Available Scenarios:", list_scenarios())

    test_type = "deadline_pressure"
    print(f"\nPattern for '{test_type}':")
    print(get_pattern(test_type))