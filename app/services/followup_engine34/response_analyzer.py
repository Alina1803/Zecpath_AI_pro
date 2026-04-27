class ResponseAnalyzer:

    def analyze(self, answer):
        answer = answer.strip()

        if len(answer) < 5:
            return "weak"

        if len(answer.split()) < 6:
            return "vague"

        if any(word in answer.lower() for word in ["example", "project", "experience"]):
            return "strong"

        return "moderate"