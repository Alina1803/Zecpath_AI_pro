import time


def optimized_response(data):

    start = time.time()

    result = {"data": data}

    latency = time.time() - start

    return {
        "result": result,
        "latency_ms": round(
            latency * 1000,
            2,
        ),
    }
