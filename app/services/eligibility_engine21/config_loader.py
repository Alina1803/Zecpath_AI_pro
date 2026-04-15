import os
import json

# 🔥 Base directory = app folder
BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../")
)

# 🔥 Correct path (app/config/)
DEFAULT_CONFIG_PATH = os.path.join(
    BASE_DIR,
    "config",
    "eligibility_rules.json"
)


def load_rules(path: str = DEFAULT_CONFIG_PATH):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Rules file not found: {path}")

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
    
def normalize_role(role: str) -> str:
    """
    Normalize role name for consistent matching
    """
    return role.strip().lower().replace(" ", "_")


def get_role_rules(role: str, rules: dict) -> dict:
    """
    Get rules for role with safe fallback
    """

    role = normalize_role(role)

    rule = rules.get(role, rules["default"])

    # Ensure all required keys exist
    rule.setdefault("min_score", 0)
    rule.setdefault("mandatory_skills", [])
    rule.setdefault("min_experience", 0)

    return rule


def reload_rules():
    """
    Reload rules dynamically (future use)
    """
    return load_rules()