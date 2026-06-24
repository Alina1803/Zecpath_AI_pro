class ConversationFlow:
    phases = [
        "introduction",
        "core",
        "evaluation",
        "completed",
    ]

    def next_phase(self, current):
        try:
            idx = self.phases.index(current)
            return self.phases[idx + 1]
        except (ValueError, IndexError):
            return "completed"
