from fastapi import APIRouter

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

router = APIRouter(
    prefix="/monitoring",
    tags=["Monitoring"],
)


# -------------------------
# System Monitoring
# -------------------------


@router.get("/run")
async def monitoring_run():

    try:

        result = monitor()

        return {
            "status": "success",
            "data": result,
        }

    except Exception as e:

        return {
            "status": "failed",
            "error": str(e),
        }


# -------------------------
# Metrics
# -------------------------


@router.get("/metrics")
async def metrics():

    return {
        "status": "success",
        "metrics": collect_metrics(),
    }


# -------------------------
# Dashboard
# -------------------------


@router.get("/dashboard")
async def dashboard_api():

    return {
        "status": "success",
        "dashboard": dashboard(),
    }


# -------------------------
# Alert Check
# -------------------------


@router.get("/alert")
async def alert():

    metric = collect_metrics()

    return {
        "status": "success",
        "alert": create_alert(metric),
    }
