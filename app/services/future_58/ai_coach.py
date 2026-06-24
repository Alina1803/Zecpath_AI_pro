class AICoach:

    @staticmethod
    def generate_feedback(scores):

        result=[]

        if scores["communication"]<70:

            result.append(
                "Improve communication"
            )

        if scores["confidence"]<65:

            result.append(
                "Build confidence"
            )

        return result