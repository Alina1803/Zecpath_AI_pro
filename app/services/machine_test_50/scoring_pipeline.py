from app.services.machine_test_50.evaluation_logic import (calculate_task_score)

from app.services.machine_test_50.scoring_engine import (time_score)

from app.services.machine_test_50.report_generator import (generate_report)


def machine_test_pipeline(data):

    score = calculate_task_score(

        data.passed,

        data.total,

        data.runtime,

        data.code_snapshot,

        data.attempts
    )

    time_factor = time_score(data.time_taken)

    final_score = (

        score["task_score"] * 0.8 +

        (time_factor * 100) * 0.2
    )

    return generate_report(

        candidate_id=data.candidate_id,

        final_score=round(final_score, 2),

        breakdown=score
    )