import traceback

from app.services.demo_45.workflow_manager import (WorkflowManager)

from app.services.hr_interview_engine_33.state_manager.interview_state import (InterviewState)


# =====================================================
# INTERVIEW CONTROLLER
# =====================================================

class InterviewController:

    def __init__(self):

        print("\n===================================")
        print("INITIALIZING INTERVIEW CONTROLLER")
        print("===================================\n")

        # =================================================
        # CORE COMPONENTS
        # =================================================

        self.workflow = WorkflowManager()

        self.state = None

        self.is_running = False

        print("Interview Controller Ready")

    # =====================================================
    # SAFE LOGGER
    # =====================================================

    def _log(self, text):

        print(f"\n{text}")

    # =====================================================
    # INITIALIZE INTERVIEW
    # =====================================================

    def initialize_interview(
        self,
        candidate_id,
        role,
        experience="experienced"
    ):

        try:

            self._log(
                "===================================")

            self._log(
                "INTERVIEW INITIALIZATION STARTED")

            self._log(
                "===================================")

            # =============================================
            # VALIDATION
            # =============================================

            if not candidate_id:

                raise ValueError(
                    "candidate_id is required"
                )

            if not role:

                raise ValueError(
                    "role is required"
                )

            experience = (
                experience or "experienced"
            )

            # =============================================
            # CREATE STATE
            # =============================================

            self.state = InterviewState(
                role=role,
                experience=experience
            )

            # =============================================
            # ATTACH CANDIDATE ID
            # =============================================

            self.state.candidate_id = (
                candidate_id
            )

            # =============================================
            # DEBUG INFO
            # =============================================

            print(f"Candidate ID : {candidate_id}")

            print(f"Role         : {role}")

            print(f"Experience   : {experience}")

            self._log(
                "INTERVIEW STATE CREATED"
            )

            return self.state

        except Exception as e:

            self._log(
                f"Interview Initialization Failed: {e}"
            )

            print(traceback.format_exc())

            return None

    # =====================================================
    # START INTERVIEW
    # =====================================================

    def start_interview(
        self,
        candidate_id,
        role,
        experience="experienced"
    ):

        try:

            self._log(
                "==================================="
            )

            self._log(
                "STARTING INTERVIEW"
            )

            self._log(
                "==================================="
            )

            # =============================================
            # PREVENT MULTIPLE RUNS
            # =============================================

            if self.is_running:

                return {

                    "status": "error",

                    "message": (
                        "Interview already running"
                    )
                }

            self.is_running = True

            # =============================================
            # INITIALIZE INTERVIEW
            # =============================================

            state = self.initialize_interview(
                candidate_id=candidate_id,
                role=role,
                experience=experience
            )

            if not state:

                raise Exception(
                    "Failed to initialize interview state"
                )

            # =============================================
            # RUN MAIN WORKFLOW
            # =============================================

            self._log(
                "RUNNING WORKFLOW MANAGER"
            )

            report = self.workflow.run(
                role=state.role,
                experience=state.experience,
                candidate_id=state.candidate_id
            )

            # =============================================
            # VALIDATE REPORT
            # =============================================

            if not report:

                raise Exception(
                    "Workflow returned empty report"
                )

            # =============================================
            # STORE REPORT
            # =============================================

            self.state.final_report = report

            self._log(
                "INTERVIEW COMPLETED SUCCESSFULLY"
            )

            return {

                "status": "success",

                "candidate_id": candidate_id,

                "report": report
            }

        except Exception as e:

            self._log(
                f"Interview Failed: {e}"
            )

            print(traceback.format_exc())

            return {

                "status": "error",

                "message": str(e)
            }

        finally:

            self.is_running = False

    # =====================================================
    # GET CURRENT STATE
    # =====================================================

    def get_state(self):

        if self.state is None:

            self._log(
                "No Active Interview State"
            )

            return None

        return self.state

    # =====================================================
    # GET CURRENT REPORT
    # =====================================================

    def get_report(self):

        if not self.state:

            return None

        return getattr(
            self.state,
            "final_report",
            None
        )

    # =====================================================
    # VALIDATE CONTROLLER
    # =====================================================

    def validate(self):

        self._log(
            "==================================="
        )

        self._log(
            "CONTROLLER VALIDATION"
        )

        self._log(
            "==================================="
        )

        print(f"Workflow Loaded : {self.workflow is not None}")

        print(f"State Exists    : {self.state is not None}")

        print(f"Running         : {self.is_running}")

        if self.state:

            print(f"Role            : {self.state.role}")

            print(f"Experience      : {self.state.experience}")

            print(f"Questions Asked : {self.state.total_questions}")

            print(f"Current Phase   : {self.state.current_phase}")

    # =====================================================
    # RESET INTERVIEW
    # =====================================================

    def reset(self):

        try:

            self._log(
                "RESETTING INTERVIEW CONTROLLER"
            )

            self.state = None

            self.is_running = False

            return {

                "status": "reset",

                "message": (
                    "Interview controller reset successful"
                )
            }

        except Exception as e:

            self._log(
                f"Reset Failed: {e}"
            )

            return {

                "status": "error",

                "message": str(e)
            }