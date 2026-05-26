from app.services.cross_round_ai_51.cross_round_engine import (calculate_final_score)

from app.services.cross_round_ai_51.ranking_engine import (rank_candidate)

from app.services.cross_round_ai_51.hiring_fit_engine import (hiring_fit)

from app.services.cross_round_ai_51.decision_engine import (hiring_decision)


# -----------------------------------
# Test Final Score Calculation
# -----------------------------------

def test_final_score():

    scores = {

        "ats": 80,

        "screening": 70,

        "hr": 75,

        "technical": 90,

        "machine_test": 85
    }

    weights = {

        "ats": 0.15,

        "screening": 0.10,

        "hr": 0.15,

        "technical": 0.35,

        "machine_test": 0.25
    }

    score = calculate_final_score(
        scores,
        weights
    )

    assert score == 82.75


# -----------------------------------
# Test Ranking Engine
# -----------------------------------

def test_ranking_engine():

    ranking = rank_candidate(85)

    assert ranking["rank"] == "A"

    assert ranking["category"] == "Strong Candidate"


# -----------------------------------
# Test Hiring Fit
# -----------------------------------

def test_hiring_fit():

    fit = hiring_fit(88)

    assert fit == "Excellent Fit"


# -----------------------------------
# Test Hiring Decision
# -----------------------------------

def test_hiring_decision():

    decision = hiring_decision(82)

    assert decision == "Hire"