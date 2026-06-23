import random
import json
import os

from app.services.hr_interview_engine_33.question_engine.category_selector import (
    CategorySelector,
)


class InterviewFlow:

    # =====================================================
    # INITIALIZATION
    # =====================================================

    def __init__(self, state, generator):

        self.state = state

        self.generator = generator

        self.selector = CategorySelector(state.role, state.experience)

        # =================================================
        # TRACK USED HR QUESTIONS
        # =================================================

        self.used_hr_questions = set()

        # =================================================
        # LOAD HR DATASET
        # =================================================

        BASE_DIR = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../../../..")
        )

        path = os.path.join(BASE_DIR, "data", "question_bank33", "hr_questions.json")

        if not os.path.exists(path):

            raise FileNotFoundError(f"HR dataset not found at: {path}")

        with open(path, "r", encoding="utf-8") as f:

            self.hr_questions = json.load(f)

        print("\n=================================")
        print("INTERVIEW FLOW INITIALIZED")
        print("=================================")

    # =====================================================
    # MAIN QUESTION FLOW
    # =====================================================

    def get_next_question(self):

        phase = self.state.current_phase

        print("\n=================================")
        print(f"CURRENT PHASE : {phase}")
        print("=================================")

        # =================================================
        # DYNAMIC CATEGORY
        # =================================================

        category = self.selector.get_category(phase)

        print(f"Selected Category : {category}")

        # =================================================
        # SMART QUESTION MIXING
        # =================================================

        for _ in range(5):

            if random.random() < 0.6:

                question = self._get_hr_question(category)

            else:

                question = self._get_role_question()

            # =============================================
            # PREVENT DUPLICATE QUESTIONS
            # =============================================

            if question and question.get("question"):

                return question

        # =================================================
        # FINAL FALLBACK
        # =================================================

        return {"type": "hr", "question": "Tell me about yourself.", "meta": None}

    # =====================================================
    # HR QUESTION HANDLER
    # =====================================================

    def _get_hr_question(self, category):

        print("\n===== HR QUESTION ENGINE =====")

        filtered = [q for q in self.hr_questions if q.get("category") == category]

        print(f"Filtered Questions : {len(filtered)}")

        # =================================================
        # REMOVE DUPLICATES
        # =================================================

        available = [
            q for q in filtered if q.get("question") not in self.used_hr_questions
        ]

        # =================================================
        # RESET IF EXHAUSTED
        # =================================================

        if not available:

            print("⚠ Resetting Used Questions")

            self.used_hr_questions.clear()

            available = filtered

        # =================================================
        # FALLBACK
        # =================================================

        if not available:

            print("⚠ No HR Questions Found")

            return {"type": "hr", "question": "Tell me about yourself.", "meta": None}

        # =================================================
        # RANDOM QUESTION
        # =================================================

        selected = random.choice(available)

        question_text = selected.get("question")

        # =================================================
        # SAFETY CHECK
        # =================================================

        if question_text in self.used_hr_questions:

            print(f"Duplicate Question Skipped:\n" f"{question_text}")

            return self._get_hr_question(category)

        self.used_hr_questions.add(question_text)

        print(f"Selected HR Question : " f"{question_text}")

        return {"type": "hr", "question": question_text, "meta": selected}

    # =====================================================
    # ROLE QUESTION HANDLER
    # =====================================================

    def _get_role_question(self):

        print("\n===== ROLE QUESTION ENGINE =====")

        try:

            q = self.generator.get_question()

            question_text = q.get("question")

            print(f"Selected Role Question : " f"{question_text}")

            return {"type": "role", "question": question_text, "meta": q}

        except Exception as e:

            print(f"⚠ Role Question Error: {e}")

            return {
                "type": "role",
                "question": "Explain your core technical skills.",
                "meta": None,
            }

    # =====================================================
    # PHASE PROGRESSION
    # =====================================================

    def progress(self):

        print("\n===== PHASE PROGRESSION =====")

        self.state.next_phase()

        print(f"Next Phase : " f"{self.state.current_phase}")

    # =====================================================
    # FOLLOW-UP HANDLING
    # =====================================================

    def handle_followup(
        self,
        q_data=None,
        answer=None,
        score=None,
        analyzer=None,
        followup_generator=None,
        decision=None,
    ):

        print("\n===== FOLLOWUP ENGINE =====")

        print(f"Question Data : {q_data}")

        print(f"Answer        : {answer}")

        print(f"Score         : {score}")

        # =================================================
        # SAFE DEFAULTS
        # =================================================

        if q_data is None:

            q_data = {}

        if answer is None:

            answer = ""

        answer = str(answer).strip()

        # =================================================
        # EMPTY ANSWER DETECTION
        # =================================================

        if answer == "":

            print("⚠ Empty Candidate Response")

            return {
                "needs_followup": True,
                "followup_question": "I could not hear your answer clearly. Can you please repeat it?",
                "level": "weak",
            }

        # =================================================
        # INVALID / SPAM ANSWER DETECTION
        # =================================================

        spam_words = ["subscribe", "like share", "hello guys", "youtube"]

        lower_answer = answer.lower()

        for spam in spam_words:

            if spam in lower_answer:

                print("⚠ Spam / Invalid Response Detected")

                return {
                    "needs_followup": True,
                    "followup_question": "Please provide a professional interview answer related to the question.",
                    "level": "weak",
                }

        # =================================================
        # SHORT ANSWER DETECTION
        # =================================================

        word_count = len(answer.split())

        print(f"Answer Word Count : {word_count}")

        if word_count <= 3:

            print("⚠ Very Short Answer Detected")

            return {
                "needs_followup": True,
                "followup_question": "Can you explain your answer in more detail?",
                "level": "weak",
            }

        # =================================================
        # ANALYZE ANSWER QUALITY
        # =================================================

        level = "medium"

        if analyzer:

            try:

                level = analyzer.analyze(answer)

            except Exception as e:

                print(f"⚠ Analyzer Failed: {e}")

                level = "medium"

        # =================================================
        # SCORE-BASED OVERRIDE
        # =================================================

        if score is not None:

            if score < 4:

                level = "weak"

            elif score < 7:

                level = "moderate"

            else:

                level = "strong"

        print(f"Detected Answer Level : {level}")

        # =================================================
        # DECISION ENGINE
        # =================================================

        should_ask = False

        if decision:

            try:

                should_ask = decision.should_followup(level)

            except Exception as e:

                print(f"⚠ Decision Engine Failed: {e}")

                should_ask = level in ["weak", "moderate"]

        else:

            should_ask = level in ["weak", "moderate"]

        print(f"Should Ask Followup : " f"{should_ask}")

        # =================================================
        # DATASET FOLLOWUP CHAIN
        # =================================================

        if should_ask and q_data.get("meta") and "follow_up_chain" in q_data["meta"]:

            try:

                followup_q = random.choice(q_data["meta"]["follow_up_chain"])

                print("✅ Dataset Followup Generated")

                return {
                    "needs_followup": True,
                    "followup_question": followup_q,
                    "level": level,
                }

            except Exception as e:

                print(f"⚠ Dataset Followup Failed: {e}")

        # =================================================
        # AI FOLLOWUP GENERATOR
        # =================================================

        if should_ask and analyzer and followup_generator:

            try:

                followup_q = followup_generator.generate(
                    q_data.get("question", ""), answer, level
                )

                print("✅ AI Followup Generated")

                return {
                    "needs_followup": True,
                    "followup_question": followup_q,
                    "level": level,
                }

            except Exception as e:

                print(f"⚠ AI Followup Failed: {e}")

        # =================================================
        # LOW SCORE DEFAULT FOLLOWUP
        # =================================================

        if score is not None and score < 5:

            print("⚠ Low Score Followup Triggered")

            return {
                "needs_followup": True,
                "followup_question": "Can you explain in more detail?",
                "level": level,
            }

        # =================================================
        # DEFAULT
        # =================================================

        print("ℹ No Followup Needed")

        return {"needs_followup": False, "followup_question": None, "level": level}
