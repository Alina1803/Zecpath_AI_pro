class ConversationState:
    def __init__(self):
        self.state = "START"

    def transition(self, action):
        if self.state == "START":
            if action == "ask_question":
                self.state = "ASKING"

        elif self.state == "ASKING":
            if action == "handle_silence":
                self.state = "WAITING"
            elif action == "evaluate_answer":
                self.state = "EVALUATING"

        elif self.state == "EVALUATING":
            self.state = "ASKING"

        elif self.state == "WAITING":
            if action == "evaluate_answer":
                self.state = "EVALUATING"

        return self.state