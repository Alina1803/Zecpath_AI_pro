from app.services.final_polish_65.ai_core.final_production_system import (
    FinalProductionSystem,
)


def test_final_system():

    result = FinalProductionSystem.process(
        {
            "candidate_id": "AI001",
            "name": "Candidate",
            "score": 86,
        }
    )

    assert result["decision"] == "Selected"
