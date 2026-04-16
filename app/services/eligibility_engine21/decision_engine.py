from app.services.eligibility_engine21.config_loader import get_role_rules
from app.services.eligibility_engine21.rules_engine import validate_candidate


# -----------------------------
# ✅ CONFIDENCE CALCULATION
# -----------------------------
def calculate_confidence(checks: dict) -> float:
    """
    Calculate confidence score based on passed checks
    """
    total_checks = len(checks)
    passed_checks = sum(1 for v in checks.values() if v)

    if total_checks == 0:
        return 0

    return round((passed_checks / total_checks) * 100, 2)


# -----------------------------
# 🚀 MAIN DECISION ENGINE
# -----------------------------
def evaluate_candidate(candidate: dict, rules: dict) -> dict:
    """
    Combines rules + validation + smart scoring
    """

    # -----------------------------
    # ✅ Step 1: Role
    # -----------------------------
    role = candidate.get("role", "default")

    # -----------------------------
    # ✅ Step 2: Rules
    # -----------------------------
    rule = get_role_rules(role, rules)

    # -----------------------------
    # ✅ Step 3: Validation
    # -----------------------------
    validation_result = validate_candidate(candidate, role, rule)
# -----------------------------
# 🔍 DEBUG (ADD HERE)
# -----------------------------
    print("\nDEBUG:")
    print("Score:", validation_result["score"])
    print("Skills:", candidate.get("skills"))
    print("Experience:", candidate.get("experience"))
    print("Checks:", validation_result["checks"])
    
    # -----------------------------
    # ✅ Step 4: Confidence
    # -----------------------------
    confidence = calculate_confidence(validation_result["checks"])

    # -----------------------------
    # 🔥 Step 5: Smart Decision
    # -----------------------------
    score = validation_result["score"]

    if score >= 60:
        status = "Highly Eligible"
    elif score >= 35:
        status = "Eligible"
    elif score >= 20:
        status = "Review"
    else:
        status = "Rejected"

    # ✅ Confidence refinement
    if status == "Review" and confidence > 75:
        status = "Eligible (Borderline)"

    # -----------------------------
    # 📊 Final Output
    # -----------------------------
    return {
        "candidate_id": candidate.get("id"),
        "role": role,
        "final_status": status,
        "confidence": confidence,
        "score": score,
        "missing_skills": validation_result["missing_skills"],
        "checks": validation_result["checks"]
    }
