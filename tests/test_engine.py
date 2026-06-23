from app.services.technical_skill_ai_47.scoring_engine import calculate_technical_score


def test_technical_engine():

    text = (
        "First I design scalable architecture, "
        "then optimize performance because "
        "real-world systems require efficiency."
    )

    result = calculate_technical_score(text, "advanced", True)

    assert result["technical_score"] > 0
