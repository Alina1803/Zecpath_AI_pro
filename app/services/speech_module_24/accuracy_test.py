from jiwer import wer

class STTAccuracy:

    def calculate_wer(self, ground_truth, predicted):
        error = wer(ground_truth, predicted)
        return {
            "wer_score": error,
            "accuracy": round((1 - error) * 100, 2)
        }