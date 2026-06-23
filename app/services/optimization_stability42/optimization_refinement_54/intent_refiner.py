class IntentRefiner:

    def detect(self, answer):

        answer = answer.lower()

        if "team" in answer:
            return "Collaborative"

        elif "lead" in answer:
            return "Leadership"

        elif "learn" in answer:
            return "Growth Mindset"

        return "Neutral"
