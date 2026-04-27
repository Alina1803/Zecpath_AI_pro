class DifficultyAdapter:

    def adjust(self, level):

        if level == "weak":
            return "easy"

        elif level == "vague":
            return "medium"

        elif level == "strong":
            return "hard"

        return "medium"