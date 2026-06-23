import logging
import traceback

from datetime import datetime
from typing import Optional, Dict, Any, List

from app.services.demo_45.workflow_manager import WorkflowManager

from app.services.demo_45.interview_controller import InterviewController

# =====================================================
# LOGGER CONFIGURATION
# =====================================================

logging.basicConfig(
    level=logging.INFO,
    format=("%(asctime)s | " "%(levelname)s | " "%(name)s | " "%(message)s"),
)

logger = logging.getLogger(__name__)

# =====================================================
# FINAL HR INTERVIEW ENGINE
# =====================================================


class FinalHRInterviewSystem:

    def __init__(self):

        logger.info("\n=====================================")

        logger.info("INITIALIZING FINAL HR INTERVIEW SYSTEM")

        logger.info("=====================================\n")

        # =============================================
        # CORE COMPONENTS
        # =============================================

        self.workflow = WorkflowManager()

        self.controller = InterviewController()

        # =============================================
        # SYSTEM STATUS
        # =============================================

        self.system_initialized = True

        logger.info("✅ FinalHRInterviewSystem Ready")

    # =================================================
    # SAFE LOGGER
    # =================================================

    def _log(self, text):

        logger.info(text)

    # =================================================
    # START INTERVIEW
    # =================================================

    def start_interview(
        self,
        candidate_id: str = "CAND_001",
        role: Optional[str] = None,
        experience: Optional[str] = None,
    ) -> Dict[str, Any]:

        start_time = datetime.now()

        self._log("\n=====================================")

        self._log("FINAL HR INTERVIEW SYSTEM STARTED")

        self._log("=====================================\n")

        # =============================================
        # VALIDATION
        # =============================================

        try:

            if not candidate_id:

                raise ValueError("candidate_id is required")

            # =========================================
            # AUTO ROLE DETECTION
            # =========================================

            if role is None:

                role = self.detect_candidate_role()

                self._log(f"🎯 Auto-detected role: {role}")

            if experience is None:

                experience = self.detect_experience_level()

                self._log(f"📊 Auto-detected experience: " f"{experience}")

            # =========================================
            # INITIALIZE CONTROLLER
            # =========================================

            self._log("🚀 Initializing Interview Controller")

            controller_state = self.controller.initialize_interview(
                candidate_id=candidate_id, role=role, experience=experience
            )

            if controller_state is None:

                raise Exception("Controller initialization returned None")

            self._log("✅ Controller Initialized")

            # =========================================
            # RUN WORKFLOW
            # =========================================

            self._log("🚀 Starting Workflow Execution")

            workflow_result = self.workflow.run(
                role=role, experience=experience, candidate_id=candidate_id
            )

            if not workflow_result:

                raise Exception("Workflow returned empty result")

            self._log("✅ Workflow Execution Completed")

            # =========================================
            # GENERATE FINAL REPORT
            # =========================================

            final_report = self.generate_final_report(
                candidate_id=candidate_id,
                role=role,
                experience=experience,
                workflow_result=workflow_result,
                started_at=start_time,
            )

            self._log("✅ Final Report Generated")

            return final_report

        except Exception as e:

            logger.exception(f"❌ Interview Failed: {e}")

            print(traceback.format_exc())

            return {
                "status": "failed",
                "candidate_id": candidate_id,
                "error": str(e),
                "timestamp": (datetime.now().isoformat()),
            }

    # =================================================
    # FINAL REPORT GENERATION
    # =================================================

    def generate_final_report(
        self,
        candidate_id: str,
        role: str,
        experience: str,
        workflow_result: Dict[str, Any],
        started_at: datetime,
    ) -> Dict[str, Any]:

        try:

            # =========================================
            # EXTRACT INTERVIEW RESULTS
            # =========================================

            interview_results = workflow_result.get("interview_results", {})

            responses = interview_results.get("responses", [])

            # =========================================
            # ANALYSIS DATA
            # =========================================

            communication_analysis = workflow_result.get("communication_analysis", {})

            behavior_analysis = workflow_result.get("behavior_analysis", {})

            voice_pipeline = workflow_result.get("voice_pipeline", {})

            summary = workflow_result.get("summary", {})

            overall_score = workflow_result.get("overall_score", 0)

            # =========================================
            # FINAL DECISION
            # =========================================

            final_decision = self._generate_final_decision(overall_score)

            # =========================================
            # INTERVIEW DURATION
            # =========================================

            ended_at = datetime.now()

            duration = str(ended_at - started_at)

            # =========================================
            # FAILED ANSWERS
            # =========================================

            failed_answers = 0

            for item in responses:

                answer = item.get("answer", "")

                if not answer or "STT Error" in str(answer):

                    failed_answers += 1

            # =========================================
            # BUILD REPORT
            # =========================================

            report = {
                # =====================================
                # SYSTEM STATUS
                # =====================================
                "status": "success",
                "generated_at": (datetime.now().isoformat()),
                # =====================================
                # CANDIDATE INFO
                # =====================================
                "candidate_id": candidate_id,
                "role": role,
                "experience": experience,
                # =====================================
                # INTERVIEW METADATA
                # =====================================
                "interview_duration": duration,
                "total_questions": len(responses),
                "failed_answers": (failed_answers),
                # =====================================
                # INTERVIEW RESPONSES
                # =====================================
                "responses": responses,
                # =====================================
                # ANALYSIS
                # =====================================
                "analysis": {
                    "overall_score": overall_score,
                    "communication_analysis": communication_analysis,
                    "behavior_analysis": behavior_analysis,
                    "voice_pipeline": voice_pipeline,
                },
                # =====================================
                # SUMMARY
                # =====================================
                "summary": summary,
                # =====================================
                # FINAL DECISION
                # =====================================
                "final_decision": final_decision,
            }

            logger.info("\n=====================================")

            logger.info("FINAL INTERVIEW REPORT GENERATED")

            logger.info("=====================================\n")

            logger.info(report)

            return report

        except Exception as e:

            logger.exception(f"❌ Report Generation Failed: {e}")

            print(traceback.format_exc())

            return {"status": "failed", "stage": "report_generation", "error": str(e)}

    # =================================================
    # FINAL DECISION LOGIC
    # =================================================

    def _generate_final_decision(self, overall_score):

        try:

            overall_score = float(overall_score)

        except:

            overall_score = 0

        if overall_score >= 8:

            return "STRONG SELECT"

        elif overall_score >= 7:

            return "SELECTED"

        elif overall_score >= 5:

            return "HOLD"

        else:

            return "REJECTED"

    # =================================================
    # ROLE DETECTION
    # =================================================

    def detect_candidate_role(self) -> str:
        """
        Future Upgrade:
        - Resume Parser
        - LLM Classification
        - JD Matching
        """

        return "backend developer"

    # =================================================
    # EXPERIENCE DETECTION
    # =================================================

    def detect_experience_level(self) -> str:
        """
        Future Upgrade:
        - Resume Analysis
        - Years Extraction
        - Skill Evaluation
        """

        return "experienced"

    # =================================================
    # SYSTEM VALIDATION
    # =================================================

    def validate_system(self):

        self._log("\n=====================================")

        self._log("SYSTEM VALIDATION")

        self._log("=====================================\n")

        print(f"Workflow Loaded : " f"{self.workflow is not None}")

        print(f"Controller Loaded : " f"{self.controller is not None}")

        print(f"System Initialized : " f"{self.system_initialized}")


# =====================================================
# CLI ENTRY
# =====================================================

if __name__ == "__main__":

    engine = FinalHRInterviewSystem()

    engine.validate_system()

    result = engine.start_interview(candidate_id="CAND_001")

    logger.info("\n=====================================")

    logger.info("FINAL OUTPUT")

    logger.info("=====================================\n")

    logger.info(result)
