from app.services.followup_engine34.difficulty__adapter import (
    DifficultyAdapter
)


class DifficultyEngine:

    def __init__(self):

        self.adapter = DifficultyAdapter()

    def adjust(self, answer_quality):

        return self.adapter.adjust(answer_quality)