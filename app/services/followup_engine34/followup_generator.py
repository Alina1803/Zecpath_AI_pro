class FollowUpGenerator:

    def generate(self, question, answer, level):

        if level == "weak":
            return f"Can you explain that in more detail?"

        elif level == "vague":
            return f"Can you give a specific example related to that?"

        elif level == "moderate":
            return f"Can you elaborate further on your answer?"

        elif level == "strong":
            return f"Can you handle a real-world scenario related to this?"

        return None