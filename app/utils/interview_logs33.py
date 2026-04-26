import os
import json
from datetime import datetime


class InterviewLogger:

    def __init__(self, log_dir="logs", session_id=None):
        self.log_dir = log_dir
        os.makedirs(self.log_dir, exist_ok=True)

        self.session_id = session_id or self._generate_session_id()
        self.log_file = os.path.join(
            self.log_dir,
            f"interview_{self.session_id}.json"
        )

        self.logs = []

    def _generate_session_id(self):
        return datetime.now().strftime("%Y%m%d_%H%M%S")

    def log_event(self, event_type, data):
        """
        Generic logger for all events
        """

        entry = {
            "timestamp": datetime.now().isoformat(),
            "session_id": self.session_id,
            "event": event_type,
            "data": data
        }

        self.logs.append(entry)

    def log_question(self, question):
        self.log_event("QUESTION", {"question": question})

    def log_answer(self, answer):
        self.log_event("ANSWER", {"answer": answer})

    def log_score(self, score):
        self.log_event("SCORE", {"score": score})

    def log_followup(self, followup):
        self.log_event("FOLLOWUP", {"question": followup})

    def log_error(self, error_msg):
        self.log_event("ERROR", {"message": error_msg})

    def save(self):
        """
        Save logs to file
        """

        with open(self.log_file, "w") as f:
            json.dump(self.logs, f, indent=4)

    def get_session_summary(self):
        """
        Useful for analytics
        """

        total_questions = len(
            [l for l in self.logs if l["event"] == "QUESTION"]
        )

        scores = [
            l["data"]["score"]
            for l in self.logs
            if l["event"] == "SCORE"
        ]

        avg_score = sum(scores) / len(scores) if scores else 0

        return {
            "session_id": self.session_id,
            "total_questions": total_questions,
            "average_score": avg_score
        }