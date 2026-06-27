from app.services.monitoring_61.metrics import (
    collect_metrics
)

from app.services.monitoring_61.alert_manager import (
    create_alert
)

def monitor():

    metric=collect_metrics()

    return {

        "metric":metric,

        "alert":
        create_alert(
            metric
        )

    }