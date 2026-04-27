class DecisionTree:

    def should_followup(self, level):
        return level in ["weak", "vague", "moderate"]