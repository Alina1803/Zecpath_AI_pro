import pytest

from app.services.eligibility_engine21.decision_engine import evaluate_candidate


# -----------------------------
# 🔧 SAMPLE RULES (MOCK CONFIG)
# -----------------------------
rules = {
    "chartered_accountant": {
        "min_score": 75,
        "mandatory_skills": ["accounting", "gst"],
        "min_experience": 2
    },
    "default": {
        "min_score": 60,
        "mandatory_skills": [],
        "min_experience": 0
    }
}


# -----------------------------
# ✅ TEST 1: FULLY ELIGIBLE
# -----------------------------
def test_eligible_candidate():
    candidate = {
        "id": "1",
        "role": "chartered_accountant",
        "score": 85,
        "skills": ["accounting", "gst", "audit"],
        "experience": 3,
        "certifications": ["CA"]
    }

    result = evaluate_candidate(candidate, rules)

    assert result["final_status"] == "Eligible"


# -----------------------------
# ⚠️ TEST 2: REVIEW CASE
# -----------------------------
def test_review_candidate():
    candidate = {
        "id": "2",
        "role": "chartered_accountant",
        "score": 78,  # passes score
        "skills": ["accounting"],  # missing GST
        "experience": 1,  # low experience
        "certifications": ["CA"]
    }

    result = evaluate_candidate(candidate, rules)

    assert result["final_status"] in ["Review", "Eligible (Borderline)"]


# -----------------------------
# ❌ TEST 3: REJECTED
# -----------------------------
def test_rejected_candidate():
    candidate = {
        "id": "3",
        "role": "chartered_accountant",
        "score": 50,  # low score
        "skills": ["excel"],
        "experience": 0,
        "certifications": []
    }

    result = evaluate_candidate(candidate, rules)

    assert result["final_status"] == "Rejected"


# -----------------------------
# 🔥 TEST 4: CERTIFICATION CHECK
# -----------------------------
def test_certification_required():
    candidate = {
        "id": "4",
        "role": "chartered_accountant",
        "score": 90,
        "skills": ["accounting", "gst"],
        "experience": 5,
        "certifications": ["b.com"]  # ❌ not CA
    }

    result = evaluate_candidate(candidate, rules)

    assert result["checks"]["certification_ok"] is False


# -----------------------------
# 🧪 TEST 5: DEFAULT ROLE
# -----------------------------
def test_default_role():
    candidate = {
        "id": "5",
        "role": "unknown_role",
        "score": 65,
        "skills": [],
        "experience": 0,
        "certifications": []
    }

    result = evaluate_candidate(candidate, rules)

    assert result["final_status"] in ["Eligible", "Review"]