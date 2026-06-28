from app.services.final_demo_63.simulation.pipeline_demo import (
    decision,
)

# -------------------
# Selected
# -------------------


def test_selected():

    assert decision(85) == "Selected"


# -------------------
# Hold
# -------------------


def test_hold():

    assert decision(65) == "Hold / Review"


# -------------------
# Rejected
# -------------------


def test_rejected():

    assert decision(40) == "Rejected"
