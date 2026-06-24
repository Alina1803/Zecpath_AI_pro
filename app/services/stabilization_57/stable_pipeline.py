from app.services.stabilization_57.stable_system import StableSystem
from app.services.stabilization_57.error_handler import ErrorHandler
from app.services.stabilization_57.stable_api import StableAPI
from app.services.stabilization_57.edge_case_handler import EdgeCaseHandler
from app.services.stabilization_57.conversation_logic_fix import ConversationFlow


class StablePipeline:

    def __init__(self):

        self.system = StableSystem()

        self.flow = ConversationFlow()

    # ----------------------------------

    def normalize_score(
        self,
        score,
    ):

        try:

            score = float(score)

        except:

            return 0

        return max(
            min(
                score,
                100,
            ),
            0,
        )

    # ----------------------------------

    def aggregate_scores(
        self,
        scores,
    ):

        cleaned = {}

        for k, v in scores.items():

            cleaned[k] = self.normalize_score(v)

        if not cleaned:

            return 0

        return round(
            sum(cleaned.values()) / len(cleaned),
            2,
        )

    # ----------------------------------

    def final_decision(
        self,
        score,
    ):

        if score >= 75:

            return "Selected"

        if score >= 55:

            return "Hold / Review"

        return "Rejected"

    # ----------------------------------

    def process_candidate(
        self,
        candidate_id,
        answer,
        scores,
    ):

        def execute():

            valid = EdgeCaseHandler.validate(answer)

            if not valid:

                return StableAPI.failed("Invalid Candidate Response")

            final_score = self.aggregate_scores(scores)

            decision = self.final_decision(final_score)

            status = self.system.monitor()

            return StableAPI.success(
                {
                    "candidate_id": candidate_id,
                    "score": final_score,
                    "decision": decision,
                    "health": status,
                    "state": "stable",
                }
            )

        return ErrorHandler.safe_run(execute)

    # ----------------------------------

    def next_phase(
        self,
        current,
    ):

        return self.flow.next_phase(current)


# ----------------------------------
# TEST
# ----------------------------------

if __name__ == "__main__":

    pipeline = StablePipeline()

    result = pipeline.process_candidate(
        candidate_id="AI001",
        answer=("I worked on debugging"),
        scores={
            "ATS": 120,
            "HR": 80,
            "VOICE": -5,
        },
    )

    print()

    print("FINAL RESULT")

    print(result)

    print()

    print("NEXT PHASE:")

    print(pipeline.next_phase("core"))
