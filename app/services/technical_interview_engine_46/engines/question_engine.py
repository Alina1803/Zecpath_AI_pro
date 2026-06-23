import json
import os
import random

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATASET_DIR = os.path.join(BASE_DIR, "datasets")


class QuestionEngine:

    def load_questions(self, filename):

        path = os.path.join(DATASET_DIR, filename)

        with open(path, "r") as file:
            return json.load(file)

    def get_question(self, skill, difficulty, filename):

        data = self.load_questions(filename)

        questions = data.get(skill, {}).get(difficulty, [])

        if not questions:
            return "No question available"

        return random.choice(questions)
