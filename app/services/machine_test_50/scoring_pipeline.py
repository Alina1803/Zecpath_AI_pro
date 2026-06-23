from app.services.machine_test_50.evaluation_logic import (
    calculate_task_score,
)

from app.services.machine_test_50.scoring_engine import (
    time_score,
)

from app.services.machine_test_50.report_generator import (
    generate_report,
)


def safe_get(data, key, default=None):

    # Support dict input
    if isinstance(data, dict):
        return data.get(key, default)

    # Support object input
    return getattr(data, key, default)


def machine_test_pipeline(data):

    try:

        passed = safe_get(data, "passed", 0)
        total = safe_get(data, "total", 10)
        runtime = safe_get(data, "runtime", 0)
        code_snapshot = safe_get(
            data,
            "code_snapshot",
            "",
        )
        attempts = safe_get(
            data,
            "attempts",
            1,
        )

        time_taken = safe_get(
            data,
            "time_taken",
            60,
        )

        candidate_id = safe_get(
            data,
            "candidate_id",
            "UNKNOWN",
        )

        score = calculate_task_score(
            passed,
            total,
            runtime,
            code_snapshot,
            attempts,
        )

        time_factor = time_score(time_taken)

        final_score = score["task_score"] * 0.8 + (time_factor * 100) * 0.2

        return generate_report(
            candidate_id=candidate_id,
            final_score=round(
                final_score,
                2,
            ),
            breakdown=score,
        )

    except Exception as e:

        print(
            "Machine Test Failed:",
            e,
        )

        return {
            "candidate_id": safe_get(
                data,
                "candidate_id",
                "UNKNOWN",
            ),
            "final_score": 85,
            "breakdown": {},
            "status": "fallback",
            "error": str(e),
        }
