import pytest

from app.services.stabilization_57.stable_pipeline import (
    StablePipeline,
)


@pytest.fixture
def pipeline():

    return StablePipeline()


# ------------------------
# NORMAL CASE
# ------------------------


def test_pipeline_success(
    pipeline,
):

    result = pipeline.process_candidate(
        candidate_id="C001",
        answer=("I improved debugging"),
        scores={
            "ATS": 120,
            "HR": 85,
            "VOICE": -5,
        },
    )

    assert result["status"] == "success"

    assert result["data"]["score"] == 61.67

    assert result["data"]["decision"] == "Hold / Review"


# ------------------------
# EMPTY ANSWER
# ------------------------


def test_empty_answer(
    pipeline,
):

    result = pipeline.process_candidate(
        candidate_id="C002",
        answer="",
        scores={"ATS": 80},
    )

    assert result["status"] == "failed"


# ------------------------
# SCORE NORMALIZATION
# ------------------------


def test_score_normalization(
    pipeline,
):

    score = pipeline.aggregate_scores(
        {
            "a": 500,
            "b": -50,
        }
    )

    assert score == 50


# ------------------------
# FINAL DECISION
# ------------------------


@pytest.mark.parametrize(
    "score,expected",
    [
        (
            90,
            "Selected",
        ),
        (
            60,
            "Hold / Review",
        ),
        (
            30,
            "Rejected",
        ),
    ],
)
def test_decision_logic(
    pipeline,
    score,
    expected,
):

    assert pipeline.final_decision(score) == expected


# ------------------------
# PHASE FLOW
# ------------------------


def test_phase_transition(
    pipeline,
):

    phase = pipeline.next_phase("core")

    assert phase == "evaluation"
