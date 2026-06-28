from app.services.final_polish_65.score_refinement import normalize_score
from app.services.final_polish_65.decision_engine import decide
from app.services.final_polish_65.recruiter_report import build_report
from app.utils.final_error_handler import safe_execute


class FinalProductionSystem:

    @staticmethod
    def process(candidate):

        def run():

            score = candidate.get("score", 0)

            refined = normalize_score(score)

            decision = decide(refined)

            report = build_report(
                candidate,
                refined,
                decision,
            )

            return {
                "status": "success",
                "candidate_id": candidate.get("candidate_id", "UNKNOWN"),
                "final_score": refined,
                "decision": decision,
                "report": report,
            }

        return safe_execute(run)
