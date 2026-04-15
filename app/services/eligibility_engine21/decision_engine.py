from app.services.eligibility_engine21.config_loader import get_role_rules
from app.services.eligibility_engine21.rules_engine import validate_candidate


def calculate_confidence(checks: dict) -> float:
    """
    Calculate confidence score based on passed checks
    """
    total_checks = len(checks)
    passed_checks = sum(1 for v in checks.values() if v)

    return round((passed_checks / total_checks) * 100, 2)


def evaluate_candidate(candidate: dict, rules: dict) -> dict:
    """
    Main Decision Engine:
    Combines rules + validation + confidence scoring
    """

    # -----------------------------
    # ✅ Step 1: Get Role
    # -----------------------------
    role = candidate.get("role", "default")

    # -----------------------------
    # ✅ Step 2: Load Role Rules
    # -----------------------------
    rule = get_role_rules(role, rules)

    # -----------------------------
    # ✅ Step 3: Validate Candidate
    # -----------------------------
    validation_result = validate_candidate(candidate, role, rule)

    # -----------------------------
    # ✅ Step 4: Confidence Score
    # -----------------------------
    confidence = calculate_confidence(validation_result["checks"])

    # -----------------------------
    # 🔥 Step 5: Final Decision Layer
    # -----------------------------
    status = validation_result["status"]

    # Optional refinement using confidence
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
        "score": validation_result["score"],
        "missing_skills": validation_result["missing_skills"],
        "checks": validation_result["checks"]
    }