class InterviewState:

    def __init__(self, role, experience):
        self.role = role
        self.experience = experience

        self.history = []                 # stores all Q&A
        self.current_phase = "introduction"
        self.current_question_id = 0

        self.followup_count = 0
        self.total_score = 0

    # ----------------------------------
    # UPDATE STATE AFTER EACH ANSWER
    # ----------------------------------
    def update(self, question_data, answer, score=0, followup=False):

        self.history.append({
            "id": self.current_question_id,
            "type": question_data.get("type"),
            "question": question_data.get("question"),
            "answer": answer,
            "score": score,
            "followup": followup
        })

        self.current_question_id += 1

        # track score
        self.total_score += score

        if followup:
            self.followup_count += 1

    # ----------------------------------
    # MOVE TO NEXT PHASE
    # ----------------------------------
    def next_phase(self):

        phases = ["introduction", "core", "evaluation", "closing"]

        current_index = phases.index(self.current_phase)

        if current_index < len(phases) - 1:
            self.current_phase = phases[current_index + 1]

    # ----------------------------------
    # FINAL RESULTS
    # ----------------------------------
    def get_results(self):

        if not self.history:
            return {"message": "No interview data available"}

        avg_score = (
            self.total_score / len(self.history)
            if self.history else 0
        )

        decision = self._final_decision(avg_score)

        return {
            "role": self.role,
            "experience": self.experience,
            "total_questions": len(self.history),
            "followups_asked": self.followup_count,
            "average_score": round(avg_score, 2),
            "decision": decision,
            "responses": self.history
        }

    # ----------------------------------
    # FINAL DECISION LOGIC
    # ----------------------------------
    def _final_decision(self, avg_score):

        if avg_score >= 7:
            return "SELECTED"
        elif avg_score >= 5:
            return "HOLD"
        else:
            return "REJECTED"