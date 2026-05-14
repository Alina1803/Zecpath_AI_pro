from app.services.demo_45.workflow_manager import (WorkflowManager)

from app.services.hr_interview_engine_33.state_manager.interview_state import (InterviewState)

# =====================================================
# INTERVIEW CONTROLLER
# =====================================================

class InterviewController:

    def __init__(self):

        self.workflow = (WorkflowManager())

        self.state = None

    def initialize_interview(
        self,
        candidate_id,
        role,
        experience="experienced"):

        print("\n===================================")

        print("INTERVIEW CONTROLLER INITIALIZED")

        print("===================================\n")

        state = InterviewState(role=role,
                experience=experience)

        state.candidate_id = (candidate_id)

        self.state = state

        print(f"Candidate ID : {candidate_id}")

        print(f"Role         : {role}")

        print(f"Experience   : {experience}")

        return state


    def start_interview(
        self,
        candidate_id,
        role,
        experience="experienced"):

        state = self.initialize_interview(
            candidate_id=candidate_id,
            role=role,
            experience=experience)

        # =============================================
        # RUN WORKFLOW
        # =============================================

        report = (
            self.workflow.run(
                role=state.role,
                experience=state.experience,
                candidate_id=state.candidate_id)
        )

        return report

    # =================================================
    # GET CURRENT STATE
    # =================================================

    def get_state(self):

        return self.state

    # =================================================
    # RESET INTERVIEW
    # =================================================

    def reset(self):

        self.state = None

        print("\nInterview Controller Reset")

        return {
            "status": "reset"
        }