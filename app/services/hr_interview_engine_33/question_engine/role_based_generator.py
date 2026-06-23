import os
import json
import random


class RoleBasedQuestionGenerator:

    def __init__(self, role, experience):

        self.role = role.lower()
        self.experience = experience

        # =====================================================
        # PROJECT ROOT
        # =====================================================

        BASE_DIR = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../../../..")
        )

        # =====================================================
        # DATASET PATH
        # =====================================================

        path = os.path.join(
            BASE_DIR, "data", "question_bank33", "role_based_generator.json"
        )

        print("DEBUG PATH:", path)

        if not os.path.exists(path):

            raise FileNotFoundError(f"Role dataset not found at: {path}")

        # =====================================================
        # LOAD QUESTIONS
        # =====================================================

        with open(path, "r", encoding="utf-8") as f:

            self.questions = json.load(f)

        # =====================================================
        # TRACK USED QUESTIONS
        # =====================================================

        self.used_questions = set()

        # =====================================================
        # FILTER QUESTIONS BY ROLE
        # =====================================================

        self.filtered = [
            q
            for q in self.questions
            if self._normalize(q.get("role", "")) == self._normalize(self.role)
        ]

        # =====================================================
        # FALLBACK PARTIAL MATCH
        # =====================================================

        if not self.filtered:

            self.filtered = [
                q
                for q in self.questions
                if self._normalize(self.role) in self._normalize(q.get("role", ""))
            ]

        # =====================================================
        # FINAL GLOBAL FALLBACK
        # =====================================================

        if not self.filtered:

            self.filtered = self.questions

    # =========================================================
    # NORMALIZE TEXT
    # =========================================================

    def _normalize(self, text):

        return text.lower().replace("_", " ").strip()

    # =========================================================
    # GET QUESTION
    # =========================================================

    def get_question(self):

        # =====================================================
        # NO QUESTIONS FOUND
        # =====================================================

        if not self.filtered:

            return {"type": "role", "question": "Explain your core technical skills."}

        # =====================================================
        # REMOVE USED QUESTIONS
        # =====================================================

        available = [
            q for q in self.filtered if q.get("question") not in self.used_questions
        ]

        # =====================================================
        # RESET IF ALL USED
        # =====================================================

        if not available:

            self.used_questions.clear()

            available = self.filtered

        # =====================================================
        # RANDOM QUESTION
        # =====================================================

        q = random.choice(available)

        question = q.get("question", "Explain your role.")

        # =====================================================
        # MARK USED
        # =====================================================

        self.used_questions.add(question)

        # =====================================================
        # EXPERIENCE-BASED ENHANCEMENT
        # =====================================================

        if str(self.experience).lower() == "experienced":

            question += " Explain with real-world examples."

        # =====================================================
        # RESPONSE
        # =====================================================

        return {"type": "role", "question": question}


# =============================================================
# TESTING
# =============================================================

if __name__ == "__main__":

    generator = RoleBasedQuestionGenerator(
        role="python developer", experience="experienced"
    )

    for _ in range(3):

        print(generator.get_question())
