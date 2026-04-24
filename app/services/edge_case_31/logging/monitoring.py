metrics = {
    "total_requests": 0,
    "failures": 0
}

def track_request():
    metrics["total_requests"] += 1

def track_failure():
    metrics["failures"] += 1

def get_metrics():
    return metrics