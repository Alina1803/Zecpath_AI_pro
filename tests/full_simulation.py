from app.services.simulation_56.candidate_generator import generate_candidates
from app.services.simulation_56.pipeline_orchestrator import PipelineOrchestrator


def test_full_simulation():

    orchestrator = PipelineOrchestrator()

    candidates = generate_candidates(50)

    results = []

    for candidate in candidates:
        results.append(orchestrator.process_candidate(candidate))

    assert len(results) == 50
