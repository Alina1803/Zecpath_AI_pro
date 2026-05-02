from app.services.hr_simulation_40.scoring_engine import calculate_score


class InterviewManager:
    def __init__(self, candidate_type: str):
        self.candidate_type = candidate_type
        self.questions = self._load_questions()
        self.responses = []

    def _load_questions(self):
        return [
            "Tell me about yourself.",
            "Why do you want this job?",
            "Describe a challenge you faced.",
            "What are your strengths?",
            "What are your weaknesses?",
            "Where do you see yourself in 5 years?"
        ]

    def _generate_answer(self, question):
        """
        Simulate candidate answers based on type
        """

        base_answers = {
            "Confident": "I have strong experience and I handled challenges effectively with clear outcomes.",
            "Hesitant": "I think maybe I can do it uh I am not completely sure but I will try my best.",
            "Inexperienced": "I am new to this but I am willing to learn and improve.",
            "Overqualified": "I have extensive experience leading complex projects and mentoring teams successfully."
        }

        return base_answers.get(self.candidate_type, "I will try my best.")

    def conduct_interview(self):
        results = []

        for question in self.questions:
            answer = self._generate_answer(question)
            score = calculate_score(answer)

            results.append({
                "question": question,
                "answer": answer,
                "score": score
            })

        self.responses = results
        return results

    def get_final_score(self):
        if not self.responses:
            return 0

        total = sum(r["score"] for r in self.responses)
        return round(total / len(self.responses), 2)

    def generate_decision(self):
        score = self.get_final_score()

        if score >= 85:
            return "Strong Hire"
        elif score >= 70:
            return "Consider"
        else:
            return "Reject"

    def run(self):
        self.conduct_interview()

        return {
            "candidate_type": self.candidate_type,
            "responses": self.responses,
            "final_score": self.get_final_score(),
            "decision": self.generate_decision()
        }