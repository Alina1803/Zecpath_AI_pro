import os
import json
import random


class RoleBasedQuestionGenerator:

    def __init__(self, role, experience):
        self.role = role.lower()
        self.experience = experience

        BASE_DIR = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../../../..")
        )

        path = os.path.join(
            BASE_DIR,
            "data",
            "question_bank33",
            "role_based_generator.json"
        )

        print("DEBUG PATH:", path)

        if not os.path.exists(path):
            raise FileNotFoundError(f"Role dataset not found at: {path}")

        with open(path, "r") as f:
            self.questions = json.load(f)

        # ✅ Track asked questions (prevents repetition)
        self.used_questions = set()

        # ✅ FILTER QUESTIONS BY ROLE
        self.filtered = [
            q for q in self.questions
            if self._normalize(q.get("role", "")) == self._normalize(self.role)
        ]

        # ✅ fallback (partial match)
        if not self.filtered:
            self.filtered = [
                q for q in self.questions
                if self._normalize(self.role) in self._normalize(q.get("role", ""))
            ]

    # ----------------------------------
    # NORMALIZATION FUNCTION
    # ----------------------------------
    def _normalize(self, text):
        return text.lower().replace("_", " ").strip()

    # ----------------------------------
    # GET QUESTION
    # ----------------------------------
    def get_question(self):

        # ❌ No questions found
        if not self.filtered:
            return {
                "type": "role",
                "question": "Explain your core technical skills."
            }

        # ✅ Avoid repetition
        available = [
            q for q in self.filtered
            if q.get("question") not in self.used_questions
        ]

        # 🔁 Reset if all used
        if not available:
            self.used_questions.clear()
            available = self.filtered

        q = random.choice(available)

        question = q.get("question", "Explain your role.")

        # ✅ Mark as used
        self.used_questions.add(question)

        # ✅ Add complexity for experienced candidates
        if self.experience == "experienced":
            question += " Explain with real-world examples."

        return {
            "type": "role",
            "question": question
        }