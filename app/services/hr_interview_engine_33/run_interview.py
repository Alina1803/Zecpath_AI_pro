import os
import json
import traceback

from datetime import datetime

from app.services.hr_interview_engine_33.state_manager.interview_state import (
    InterviewState,
)

from app.services.hr_interview_engine_33.question_engine.role_based_generator import (
    RoleBasedQuestionGenerator,
)

from app.services.hr_interview_engine_33.flow_engine.interview_flow import InterviewFlow

from app.services.screening_engine_26.scoring_engine import AdvancedScoringEngine

from app.services.voice_ai_45.voice_pipeline import VoiceInterviewPipeline

# =========================================================
# CONFIG
# =========================================================

OUTPUT_DIR = os.path.join("data", "processed", "output_33")

DOMAIN_BASE_PATH = os.path.join("data", "domain_knowledge")

# =========================================================
# HELPERS
# =========================================================


def create_output_dir():

    os.makedirs(OUTPUT_DIR, exist_ok=True)


def save_results(data):

    create_output_dir()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    file_path = os.path.join(OUTPUT_DIR, f"interview_{timestamp}.json")

    with open(file_path, "w", encoding="utf-8") as f:

        json.dump(data, f, indent=4)

    print(f"\nResults saved to: {file_path}")


# =========================================================
# HR SCORING
# =========================================================


def simple_hr_score(answer):

    if not answer:

        return 0

    answer = str(answer).strip().lower()

    invalid_answers = [
        ".",
        ". .",
        "...",
        "music",
        "music music",
        "bang",
        "bang!",
        "noise",
        "test",
        "hello",
    ]

    if answer in invalid_answers:

        return 0

    words = answer.split()

    word_count = len(words)

    if word_count < 3:

        return 1

    elif word_count < 8:

        return 3

    elif word_count < 15:

        return 5

    elif word_count < 30:

        return 7

    return 9


# =========================================================
# FOLLOWUP DECISION
# =========================================================


class SimpleDecision:

    def should_followup(self, level):

        return level == "low"


# =========================================================
# LEGACY INTERVIEW ENGINE
# =========================================================


class LegacyInterviewEngine:

    def __init__(self):

        self.total_questions = 6

        self.max_duplicate_retries = 10

        self.voice_pipeline = VoiceInterviewPipeline()

    # =====================================================
    # CLEAN TRANSCRIPT
    # =====================================================

    def clean_transcript(self, text):

        if not text:

            return ""

        text = str(text).strip()

        invalid = [".", ". .", "...", "music", "music music", "bang!", "noise"]

        if text.lower() in invalid:

            return ""

        return text

    # =====================================================
    # UNIQUE QUESTION CHECK
    # =====================================================

    def _get_unique_question(self, flow, state):

        retries = 0

        while retries < self.max_duplicate_retries:

            q_data = flow.get_next_question()

            if not q_data:

                return None

            question = q_data.get("question", "").strip()

            # =============================================
            # DUPLICATE CHECK
            # =============================================

            if not state.has_asked_question(question):

                return q_data

            print(f"\nDuplicate Question Skipped:\n" f"{question}")

            retries += 1

        raise Exception("Unable to generate unique question")

    # =====================================================
    # LOAD SCORING ENGINE
    # =====================================================

    def load_scoring_engine(self, role):

        try:

            base_path = os.path.join(DOMAIN_BASE_PATH, role.lower())

            domain_path = os.path.join(base_path, "domain.json")

            prompt_path = os.path.join(base_path, "prompt.txt")

            if not os.path.exists(domain_path) or not os.path.exists(prompt_path):

                print("⚠ Scoring files not found")

                return None

            with open(domain_path, "r") as f:

                domain_data = json.load(f)

            with open(prompt_path, "r") as f:

                prompt_template = f.read()

            scoring_engine = AdvancedScoringEngine(domain_data, prompt_template)

            print("✅ Scoring Engine Initialized")

            return scoring_engine

        except Exception as e:

            print(f"⚠ Scoring Engine Disabled: {e}")

            return None

    # =====================================================
    # MAIN RUN
    # =====================================================

    def run(self, role, experience):

        print("\n===== HR Interview Engine Started =====\n")

        # =================================================
        # STATE
        # =================================================

        state = InterviewState(role=role, experience=experience)

        # =================================================
        # QUESTION GENERATOR
        # =================================================

        generator = RoleBasedQuestionGenerator(role, experience)

        # =================================================
        # FLOW ENGINE
        # =================================================

        flow = InterviewFlow(state, generator)

        # =================================================
        # SCORING ENGINE
        # =================================================

        scoring_engine = self.load_scoring_engine(role)

        # =================================================
        # FOLLOWUP DECISION
        # =================================================

        decision_engine = SimpleDecision()

        print("\n--- Interview Started ---")

        # =================================================
        # MAIN INTERVIEW LOOP
        # =================================================

        for i in range(self.total_questions):

            print(f"\nPhase: " f"{state.current_phase.upper()}")

            # =============================================
            # GET QUESTION
            # =============================================

            try:

                q_data = self._get_unique_question(flow, state)

            except Exception as e:

                print(f"\nQuestion Generation Failed: {e}")

                break

            if not q_data:

                print("\nNo valid question available.")

                break

            question_text = q_data.get("question", "No question")

            q_type = q_data.get("type", "unknown")

            print(f"\nQ{i + 1} " f"[{q_type.upper()}]: " f"{question_text}")

            # =============================================
            # VOICE PIPELINE
            # =============================================

            answer = ""

            transcript = ""

            audio_path = None

            try:

                print("\nAI HR is asking question...")

                voice_result = self.voice_pipeline.process_question(
                    question=question_text, question_id=i + 1, duration=20
                )

                print("\nVOICE PIPELINE RESULT\n")

                print(json.dumps(voice_result, indent=4))

                transcript = voice_result.get("transcript", "")

                transcript = self.clean_transcript(transcript)

                answer = transcript

                audio_path = voice_result.get("audio_path")

                print(f"\nCandidate Answer:\n" f"{answer}")

            except Exception as e:

                print(f"\nVoice Pipeline Failed: {e}")

                print(traceback.format_exc())

            # =============================================
            # EMPTY ANSWER
            # =============================================

            if not answer:

                print("\n⚠ No valid candidate response captured.")

            # =============================================
            # SCORING
            # =============================================

            score = 0

            try:

                # =========================================
                # INVALID ANSWER
                # =========================================

                if not answer:

                    score = 0

                elif len(answer.split()) < 2:

                    score = 1

                else:

                    # =====================================
                    # HR QUESTIONS
                    # =====================================

                    if q_type == "hr":

                        score = simple_hr_score(answer)

                    # =====================================
                    # ROLE QUESTIONS
                    # =====================================

                    else:

                        if scoring_engine:

                            score = scoring_engine.evaluate(question_text, answer)

                            if score is None:

                                score = simple_hr_score(answer)

                        else:

                            score = simple_hr_score(answer)

                # =========================================
                # SEMANTIC BONUS
                # =========================================

                relevant_keywords = [
                    "project",
                    "team",
                    "system",
                    "api",
                    "database",
                    "debug",
                    "experience",
                    "backend",
                    "python",
                    "fastapi",
                ]

                matches = sum(1 for k in relevant_keywords if k in answer.lower())

                score += matches * 0.5

                if score > 10:

                    score = 10

                score = round(score, 2)

            except Exception as e:

                print(f"Scoring Failed: {e}")

                score = 0

            print(f"\nCalculated Score: {score}")

            # =============================================
            # UPDATE STATE
            # =============================================

            state.update(
                q_data=q_data,
                answer=answer,
                transcript=transcript,
                audio_path=audio_path,
                communication_score=score,
                confidence_score=score,
                technical_score=score,
                behavioral_score=score,
            )

            # =============================================
            # FOLLOWUP ENGINE
            # =============================================

            try:

                result = flow.handle_followup(
                    q_data=q_data,
                    answer=answer,
                    analyzer=None,
                    followup_generator=None,
                    decision=decision_engine,
                )

                followup = None

                level = "unknown"

                # =========================================
                # SAFE RESULT HANDLING
                # =========================================

                if isinstance(result, tuple):

                    if len(result) >= 1:

                        followup = result[0]

                    if len(result) >= 2:

                        level = result[1]

                elif isinstance(result, str):

                    followup = result

                # =========================================
                # ASK FOLLOWUP
                # =========================================

                if followup:

                    if state.has_asked_question(followup):

                        print("\nDuplicate Follow-up Skipped")

                    else:

                        print(f"\nFollow-up Question:\n" f"{followup}")

                        try:

                            followup_voice = self.voice_pipeline.process_question(
                                question=followup,
                                question_id=f"followup_{i + 1}",
                                duration=10,
                            )

                            fu_answer = followup_voice.get("transcript", "")

                            fu_answer = self.clean_transcript(fu_answer)

                            print(f"\nFollow-up Answer:\n" f"{fu_answer}")

                            state.update(
                                q_data={"question": followup, "type": "followup"},
                                answer=fu_answer,
                                transcript=fu_answer,
                                audio_path=None,
                                communication_score=score,
                                confidence_score=score,
                                technical_score=score,
                                behavioral_score=score,
                            )

                        except Exception as e:

                            print(f"\nFollow-up Voice Failed: {e}")

            except Exception as e:

                print(f"\nFollow-up Handling Failed: {e}")

            # =============================================
            # NEXT PHASE
            # =============================================

            flow.progress()

        # =====================================================
        # INTERVIEW COMPLETED
        # =====================================================

        print("\n--- Interview Completed ---\n")

        results = state.get_results()

        # =====================================================
        # FINAL DECISION
        # =====================================================

        avg_score = results.get("average_score", 0)

        if avg_score >= 8:

            results["decision"] = "SELECT"

        elif avg_score >= 5:

            results["decision"] = "HOLD"

        else:

            results["decision"] = "REJECT"

        print("===== INTERVIEW SUMMARY =====")

        print(json.dumps(results, indent=4))

        save_results(results)

        return results


# =========================================================
# CLI RUNNER
# =========================================================


def run():

    role = input("Enter role: ").strip().lower()

    experience = input("Enter experience " "(fresher/experienced): ").strip().lower()

    engine = LegacyInterviewEngine()

    engine.run(role=role, experience=experience)


# =========================================================
# MAIN
# =========================================================

if __name__ == "__main__":

    run()
