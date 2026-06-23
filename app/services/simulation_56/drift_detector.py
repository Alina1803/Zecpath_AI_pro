import statistics


class DriftDetector:

    @staticmethod
    def detect(score_runs):

        stdev = statistics.stdev(score_runs)

        return {
            "scores": score_runs,
            "std_dev": round(stdev, 2),
            "drift_detected": stdev > 5,
        }
