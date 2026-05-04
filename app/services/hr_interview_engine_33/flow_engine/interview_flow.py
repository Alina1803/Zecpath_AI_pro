import random
import json
import os

from app.services.hr_interview_engine_33.question_engine.category_selector import CategorySelector


class InterviewFlow:

    def __init__(self, state, generator):
        self.state = state
        self.generator = generator
        self.selector = CategorySelector(state.role, state.experience)

        # ✅ Track asked HR questions (prevents repetition)
        self.used_hr_questions = set()

        # ✅ Load HR dataset
        BASE_DIR = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../../../..")
        )

        path = os.path.join(
            BASE_DIR, "data", "question_bank33", "hr_questions.json"
        )

        if not os.path.exists(path):
            raise FileNotFoundError(f"HR dataset not found at: {path}")

        with open(path, "r") as f:
            self.hr_questions = json.load(f)

    # ----------------------------------
    # MAIN QUESTION FLOW
    # ----------------------------------
    def get_next_question(self):

        phase = self.state.current_phase

        # ✅ Get category dynamically
        category = self.selector.get_category(phase)

        # ✅ Smarter mix (avoid too many HR in a row)
        if random.random() < 0.6:
            return self._get_hr_question(category)
        else:
            return self._get_role_question()

    # ----------------------------------
    # HR QUESTION HANDLER
    # ----------------------------------
    def _get_hr_question(self, category):

        filtered = [
            q for q in self.hr_questions
            if q.get("category") == category
        ]

        # ✅ Remove already used questions
        available = [
            q for q in filtered
            if q.get("question") not in self.used_hr_questions
        ]

        # 🔁 Reset if exhausted
        if not available:
            self.used_hr_questions.clear()
            available = filtered

        # ❌ Still empty → fallback
        if not available:
            return {
                "type": "hr",
                "question": "Tell me about yourself.",
                "meta": None
            }

        selected = random.choice(available)

        # ✅ Mark as used
        self.used_hr_questions.add(selected.get("question"))

        return {
            "type": "hr",
            "question": selected.get("question"),
            "meta": selected
        }

    # ----------------------------------
    # ROLE-BASED QUESTION HANDLER
    # ----------------------------------
    def _get_role_question(self):

        try:
            q = self.generator.get_question()
            return { 
                "type": "role",
                "question": q.get("question"),
                "meta": None
            }
        except Exception as e:
            print(f"⚠ Role question error: {e}")
            return {
                "type": "role",
                "question": "Explain your core technical skills.",
                "meta": None
            }

    # ----------------------------------
    # PHASE PROGRESSION
    # ----------------------------------
    def progress(self):
        self.state.next_phase()

    # ----------------------------------
    # FOLLOW-UP HANDLING
    # ----------------------------------
    def handle_followup(self, question_data, answer, analyzer=None, followup_generator=None, decision=None):

        # ✅ Safe analyzer
        if analyzer:
            try:
                level = analyzer.analyze(answer)
            except Exception:
                level = "medium"
        else:
            level = "medium"

        # ✅ Decision logic
        if decision:
            try:
                should_ask = decision.should_followup(level)
            except Exception:
                should_ask = False
        else:
            should_ask = (level == "low")

        # ✅ Dataset follow-up
        if (
            should_ask and
            question_data.get("meta") and
            "follow_up_chain" in question_data["meta"]
        ):
            return random.choice(question_data["meta"]["follow_up_chain"]), level

        # ✅ AI fallback
        if should_ask and analyzer and followup_generator:
            try:
                followup_q = followup_generator.generate(
                    question_data["question"], answer, level
                )
                return followup_q, level
            except Exception:
                pass

        return None, level