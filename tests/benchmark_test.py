from app.services.simulation_56.drift_detector import DriftDetector


def test_drift_detector():

    runs = [80, 82, 79, 81, 83]

    result = DriftDetector.detect(runs)

    assert result["drift_detected"] is False
