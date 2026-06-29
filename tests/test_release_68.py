from app.services.release_ready_68.ai_core.release_ready_system import (
    ReleaseReadySystem,
)


def test_release():

    output = ReleaseReadySystem.process(
        {"candidate_id": "AI001", "name": "Zeit", "score": 88}
    )

    assert output["status"] == "success"
