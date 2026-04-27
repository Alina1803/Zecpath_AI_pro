class InterviewState:

    def __init__(self, role, experience):
        self.role = role
        self.experience = experience
        self.history = []
        self.current_phase = "introduction"
        self.current_question_id = 0

    def update(self, question, answer, score=None):
        self.history.append({
            "id": self.current_question_id,
            "question": question,
            "answer": answer,
            "score": score
        })
        self.current_question_id += 1

    def next_phase(self):
        phases = ["introduction", "core", "evaluation", "closing"]
        current_index = phases.index(self.current_phase)

        if current_index < len(phases) - 1:
            self.current_phase = phases[current_index + 1]

    def get_results(self):
        if not self.history:
            return {"message": "No interview data available"}

        return {
            "role": self.role,
            "experience": self.experience,
            "total_questions": len(self.history),
            "responses": self.history
        }
    def __init__(self, role, experience):
        self.role = role
        self.experience = experience
        self.history = []
        self.current_phase = "introduction"
        self.followup_count = 0

    def update(self, question, answer, score, followup=False):
        self.history.append({
            "question": question,
            "answer": answer,
            "score": score,
            "followup": followup
        })