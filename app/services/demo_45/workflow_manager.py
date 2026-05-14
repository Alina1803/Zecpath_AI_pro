from app.services.hr_interview_engine_33.run_interview import (LegacyInterviewEngine)
from app.services.followup_engine34.run_pipeline34 import (LegacyFollowupPipeline)
from app.services.voice_ai_45.voice_pipeline import (VoiceInterviewPipeline)
from app.services.communication_engine35.communication_engine import (CommunicationEngine)
from app.services.stress_conf_analyzer36.run_analyzer import (analyze_behavior)
from app.services.summary_39.summary_generator import (generate_interview_summary)

# =====================================================
# WORKFLOW MANAGER
# =====================================================

class WorkflowManager:

    def __init__(self):

        self.legacy_engine = (
            LegacyInterviewEngine())

        self.followup_engine = (
            LegacyFollowupPipeline())

        self.voice_pipeline = (
            VoiceInterviewPipeline())

        self.communication = (
            CommunicationEngine())

    # =================================================
    # MAIN WORKFLOW
    # =================================================

    def run(
        self,
        role="backend developer",
        experience="experienced",
        candidate_id="CAND_001"
    ):

        print("\n===== WORKFLOW MANAGER STARTED =====\n")
        # =====================================
        # RUN INTERVIEW ENGINE
        # =====================================

        results = (
            self.legacy_engine.run(
                role=role,
                experience=experience)
        )

        # =====================================
        # VOICE PIPELINE
        # =====================================

        voice_result = None

        try:

            voice_result = (
                self.voice_pipeline.process_question(
                    question="Tell me about yourself",
                    question_id=1,
                    duration=10)
            )

            print("\nVOICE PIPELINE RESULT\n")
            print(voice_result)

        except Exception as e:

            print(f"Voice Pipeline Failed: {e}")

        # =====================================
        # PREPARE TRANSCRIPTS
        # =====================================

        sample_text = ""

        try:

            if (
                results
                and
                "answers" in results
            ):

                answers = results.get(
                    "answers",
                    []
                )

                transcripts = []

                for item in answers:

                    if isinstance(item, dict):

                        transcript = item.get(
                            "answer",
                            ""
                        )

                        transcripts.append(
                            transcript
                        )

                sample_text = " ".join(
                    transcripts
                )

        except Exception as e:

            print(
                f"Transcript Processing Failed: {e}")
        # =====================================
        # COMMUNICATION ANALYSIS
        # =====================================

        communication_result = None

        try:

            if sample_text:

                communication_result = (
                    self.communication.evaluate(
                        sample_text)
                )

                print("\nCommunication Analysis\n")

                print(communication_result)

        except Exception as e:

            print(f"Communication Analysis Failed: {e}")

        # =====================================
        # BEHAVIOR ANALYSIS
        # =====================================

        behavior_result = None

        try:

            if sample_text:

                behavior_result = (
                    analyze_behavior(
                        text=sample_text,
                        duration=60,
                        save=True
                    )
                )

                print("\nBehavior Analysis\n")

                print(behavior_result)

        except Exception as e:

            print(f"Behavior Analysis Failed: {e}")

        # =====================================
        # OVERALL SCORE
        # =====================================

        overall_score = 0

        try:

            if (
                results
                and
                "scores" in results
            ):

                scores = results.get(
                    "scores",
                    []
                )

                if scores:

                    overall_score = (
                        sum(scores) / len(scores)
                    )

        except Exception as e:

            print(f"Score Calculation Failed: {e}")

        # =====================================
        # SUMMARY
        # =====================================

        summary = {}

        try:

            summary = (
                generate_interview_summary(
                    candidate_id=candidate_id,
                    role=role,
                    final_score=overall_score
                )
            )

        except Exception as e:

            print(f"Summary Generation Failed: {e}")

        # =====================================
        # FINAL OUTPUT
        # =====================================

        final_output = {

            "candidate_id": candidate_id,

            "role": role,

            "experience": experience,

            "overall_score": overall_score,

            "interview_results": results,

            "voice_pipeline": voice_result,

            "communication_analysis": (communication_result),

            "behavior_analysis": (behavior_result),

            "summary": summary
        }

        print("\n===== WORKFLOW COMPLETED =====\n")

        return final_output