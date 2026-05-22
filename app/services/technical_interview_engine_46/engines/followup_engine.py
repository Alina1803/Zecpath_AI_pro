from app.services.followup_engine34.followup_generator import (
    FollowUpGenerator
)


class FollowUpEngine:

    def __init__(self):

        self.generator = FollowUpGenerator()

    def generate(self, question, answer, level):

        return self.generator.generate(
            question,
            answer,
            level
        )