from app.services.release_ready_68.final_scoring.score_refinement import (
    normalize_score,
)

from app.services.release_ready_68.recruiter_outputs.report import (
    generate_report,
)

from app.utils.final_error_handler import (
    safe_execute,
)


class ReleaseReadySystem:

    @staticmethod
    def process(candidate):

        def execute():

            score = normalize_score(candidate["score"])

            decision = "Selected" if score >= 75 else "Hold"

            report = generate_report(
                candidate,
                score,
                decision,
            )

            return {
                "status": "success",
                "candidate_id": candidate["candidate_id"],
                "final_score": score,
                "decision": decision,
                "report": report,
            }

        return safe_execute(execute)
