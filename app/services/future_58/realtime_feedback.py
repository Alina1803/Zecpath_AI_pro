class RealtimeFeedback:

    @staticmethod
    def analyze(score):

        if score < 70:

            return {

                "feedback":
                "Improve clarity"

            }

        return {

            "feedback":
            "Excellent"

        }