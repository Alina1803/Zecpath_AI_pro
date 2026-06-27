from app.services.monitoring_61.metrics import (
    collect_metrics,
)

from app.services.monitoring_61.alert_manager import (
    create_alert,
)

from app.services.monitoring_61.dashboard import (
    dashboard,
)

from app.services.monitoring_61.observability_engine import (
    monitor,
)

# --------------------------------
# Metrics Test
# --------------------------------


def test_metrics():

    result = collect_metrics()

    assert result["response_ms"] > 0

    assert result["accuracy"] >= 0


# --------------------------------
# Alert Test
# --------------------------------


def test_alert():

    metric = {"failures": 2}

    result = create_alert(metric)

    assert result in [
        "OK",
        "ALERT",
    ]


# --------------------------------
# Dashboard Test
# --------------------------------


def test_dashboard():

    result = dashboard()

    assert result["processed"] >= 0

    assert result["success_rate"] > 0


# --------------------------------
# Monitoring Engine Test
# --------------------------------


def test_monitor():

    result = monitor()

    assert "metric" in result

    assert "alert" in result


# --------------------------------
# Full Monitoring Validation
# --------------------------------


def test_complete_monitoring():

    result = monitor()

    assert result["alert"] in [
        "OK",
        "ALERT",
    ]


# --------------------------------
# Run Without Pytest
# --------------------------------

if __name__ == "__main__":

    test_metrics()

    test_alert()

    test_dashboard()

    test_monitor()

    test_complete_monitoring()

    print("\nALL MONITORING TESTS PASSED\n")
