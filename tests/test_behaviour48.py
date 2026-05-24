from app.services.behavioural_engine48.signal_mapping import (
    calculate_behavior_score
)


def test_behavior_score():

    result = calculate_behavior_score({

        "eye_focus": 0.8,
        "head_stability": 0.7,
        "engagement": 0.9,
        "distraction": 0.2
    })

    assert result > 0