from app.services.demo_45.workflow_manager import (WorkflowManager)

from app.services.demo_45.interview_controller import (InterviewController)

# =====================================================
# FINAL HR INTERVIEW ENGINE
# =====================================================

class FinalHRInterviewSystem:

    def __init__(self):

        
        self.workflow = (
            WorkflowManager())


        self.controller = (
            InterviewController())

    # =================================================
    # START INTERVIEW
    # =================================================

    def start_interview(
        self,
        candidate_id="CAND_001",
        role="backend developer",
        experience="experienced"):

        print("\n=====================================")

        print("FINAL HR INTERVIEW SYSTEM STARTED")

        print("=====================================\n")

        # =====================================
        # CONTROLLER START
        # =====================================

        try:

            self.controller.initialize_interview(
                candidate_id=candidate_id,
                role=role,
                experience=experience)

        except Exception as e:

            print(f"Controller Initialization Failed: {e}")

        # =====================================
        # RUN WORKFLOW
        # =====================================

        try:

            result = (
                self.workflow.run(
                    role=role,
                    experience=experience,
                    candidate_id=candidate_id))

            print("\n=====================================")

            print("FINAL INTERVIEW RESULT")

            print("=====================================\n")

            print(result)

            return result

        except Exception as e:

            print(f"\nWorkflow Execution Failed: {e}")

            return {
                "status": "failed",
                "error": str(e)
            }


# =====================================================
# CLI ENTRY
# =====================================================

if __name__ == "__main__":

    engine = (FinalHRInterviewSystem())

    result = engine.start_interview(
        candidate_id="CAND_001",
        role="backend developer",
        experience="experienced")

    print("\n=====================================")

    print("FINAL OUTPUT")

    print("=====================================\n")

    print(result)