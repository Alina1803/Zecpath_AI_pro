from app.services.hr_interview_engine_33.run_interview import (LegacyInterviewEngine)
from app.services.followup_engine34.run_pipeline34 import (LegacyFollowupPipeline)
from app.services.voice_ai_45.voice_pipeline import (VoiceInterviewPipeline)
from app.services.communication_engine35.communication_engine import (CommunicationEngine)
from app.services.stress_conf_analyzer36.run_analyzer import (analyze_behavior)
from app.services.summary_39.summary_generator import (generate_interview_summary)

import traceback


# =====================================================
# WORKFLOW MANAGER
# =====================================================

class WorkflowManager:

    def __init__(self):

        print("\n=================================")
        print("INITIALIZING WORKFLOW MANAGER")
        print("=================================")

        # =================================================
        # CORE ENGINES
        # =================================================

        self.legacy_engine = (LegacyInterviewEngine())

        self.followup_engine = (LegacyFollowupPipeline())

        self.voice_pipeline = (VoiceInterviewPipeline())

        self.communication = (CommunicationEngine())

        print("Workflow Manager Ready")

    # =================================================
    # SAFE PRINT
    # =================================================

    def _log(self, text):

        print(f"\n{text}")

    # =================================================
    # EXTRACT TRANSCRIPTS
    # =================================================

    def _extract_transcripts(self, results):

        transcripts = []

        try:

            if not results:

                return transcripts

            responses = results.get(
                "responses",
                [])

            for item in responses:

                if not isinstance(item, dict):

                    continue

                transcript = item.get("transcript","")

                answer = item.get("answer","")

                # =====================================
                # PRIORITY TO TRANSCRIPT
                # =====================================

                if (
                    transcript and
                    isinstance(transcript, str)):

                    transcripts.append(
                        transcript.strip())

                # =====================================
                # FALLBACK TO ANSWER
                # =====================================

                elif (
                    answer and
                    isinstance(answer, str)):

                    if "STT Error" not in answer:

                        transcripts.append(
                            answer.strip())

        except Exception as e:

            self._log(
                f"Transcript Extraction Failed: {e}")

        return transcripts

    # =================================================
    # CALCULATE OVERALL SCORE
    # =================================================

    def _calculate_overall_score(self, results):

        try:

            if not results:

                return 0

            responses = results.get(
                "responses",
                [])

            scores = []

            for item in responses:

                if not isinstance(item, dict):

                    continue

                score = item.get(
                    "final_score",0)

                if isinstance(score, (int, float)):

                    scores.append(score)

            if not scores:

                return 0

            return round(
                sum(scores) / len(scores),2)

        except Exception as e:

            self._log(
                f"Score Calculation Failed: {e}")

            return 0

    # =================================================
    # MAIN WORKFLOW
    # =================================================

    def run(
        self,
        role="backend developer",
        experience="experienced",
        candidate_id="CAND_001"
    ):

        self._log("===== WORKFLOW MANAGER STARTED =====")

        # =================================================
        # DEFAULT OUTPUTS
        # =================================================

        results = {}

        voice_result = None

        communication_result = None

        behavior_result = None

        summary = {}

        overall_score = 0

        sample_text = ""

        # =================================================
        # RUN MAIN INTERVIEW ENGINE
        # =================================================

        try:

            self._log("STARTING INTERVIEW ENGINE")

            results = (
                self.legacy_engine.run(
                    role=role,
                    experience=experience))

            self._log("INTERVIEW ENGINE COMPLETED")

        except Exception as e:

            self._log(
                f"Interview Engine Failed: {e}")

            print(traceback.format_exc())

        # =================================================
        # VALIDATE RESULTS
        # =================================================

        if not results:

            results = {}

        # =================================================
        # DEBUG RESULTS
        # =================================================

        self._log("INTERVIEW RESULTS")

        print(results)

        # =================================================
        # OPTIONAL VOICE PIPELINE TEST
        # =================================================

        try:

            self._log("STARTING VOICE PIPELINE")

            voice_result = (
                self.voice_pipeline.process_question(
                    question="Tell me about yourself",
                    question_id=1,
                    duration=10))

            self._log("VOICE PIPELINE RESULT")

            print(voice_result)

        except Exception as e:

            self._log(f"Voice Pipeline Failed: {e}")

            print(traceback.format_exc())

        # =================================================
        # EXTRACT TRANSCRIPTS
        # =================================================

        try:

            transcripts = (
                self._extract_transcripts(
                    results))

            sample_text = " ".join(transcripts)

            self._log("EXTRACTED TRANSCRIPTS")

            print(sample_text)

        except Exception as e:

            self._log(f"Transcript Processing Failed: {e}")

            print(traceback.format_exc())

        # =================================================
        # COMMUNICATION ANALYSIS
        # =================================================

        try:

            if sample_text.strip():

                self._log("RUNNING COMMUNICATION ANALYSIS")

                communication_result = (
                    self.communication.evaluate(
                        sample_text))

                self._log("COMMUNICATION ANALYSIS RESULT")

                print(communication_result)

            else:

                self._log(
                    "Skipping Communication Analysis "
                    "(No Transcript Available)")

        except Exception as e:

            self._log(
                f"Communication Analysis Failed: {e}")

            print(traceback.format_exc())

        # =================================================
        # BEHAVIOR ANALYSIS
        # =================================================

        try:

            if sample_text.strip():

                self._log(
                    "RUNNING BEHAVIOR ANALYSIS")

                behavior_result = (
                    analyze_behavior(
                        text=sample_text,
                        duration=60,
                        save=True))

                self._log(
                    "BEHAVIOR ANALYSIS RESULT")

                print(behavior_result)

            else:

                self._log(
                    "Skipping Behavior Analysis "
                    "(No Transcript Available)")

        except Exception as e:

            self._log(
                f"Behavior Analysis Failed: {e}")

            print(traceback.format_exc())

        # =================================================
        # OVERALL SCORE
        # =================================================

        overall_score = (
            self._calculate_overall_score(
                results))

        self._log(f"OVERALL SCORE : {overall_score}")

        # =================================================
        # SUMMARY GENERATION
        # =================================================

        try:

            self._log("GENERATING INTERVIEW SUMMARY")

            summary = (
                generate_interview_summary(
                    candidate_id=candidate_id,
                    role=role,
                    final_score=overall_score))

        except Exception as e:

            self._log(f"Summary Generation Failed: {e}")

            print(traceback.format_exc())

        # =================================================
        # FINAL OUTPUT
        # =================================================

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

        self._log("===== WORKFLOW COMPLETED =====")

        return final_output