from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score


class AIHumanComparison:

    @staticmethod
    def compare(ai_results, human_results):

        ai = [x["decision"] for x in ai_results]
        human = [x["decision"] for x in human_results]

        ai_binary = [1 if x == "Selected" else 0 for x in ai]

        human_binary = [1 if x == "Selected" else 0 for x in human]

        return {
            "accuracy": accuracy_score(human_binary, ai_binary),
            "precision": precision_score(human_binary, ai_binary),
            "recall": recall_score(human_binary, ai_binary),
            "f1": f1_score(human_binary, ai_binary),
        }
