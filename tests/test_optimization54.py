from app.services.optimization_stability42.optimization_refinement_54.optimization_pipeline import (
    OptimizationPipeline,
)


def test_optimization():

    sample = {
        "score": 85,
        "integrity_risk": "High Risk",
        "ats": 90,
        "technical": 40,
        "hr": 85,
        "communication": 35,
        "answer": "I love working with team members",
    }

    result = OptimizationPipeline().run(sample)

    assert result["optimization_status"] == "Completed"

    print("Day 54 Optimization Test Passed")
