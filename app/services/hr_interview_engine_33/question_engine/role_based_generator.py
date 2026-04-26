import random
import json

class RoleBasedQuestionGenerator:

    def __init__(self, role, experience):
        self.role = role
        self.experience = experience

        with open("data/question_bank33/hr_questions.json") as f:
            self.questions = json.load(f)

    def get_question(self, category):
        base_questions = self.questions.get(category, [])

        if self.experience == "fresher":
            return random.choice(base_questions)

        elif self.experience == "experienced":
            return random.choice(base_questions) + " Explain with examples."

        return random.choice(base_questions)