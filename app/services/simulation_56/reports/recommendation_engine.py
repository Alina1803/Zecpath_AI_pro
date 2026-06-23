class RecommendationEngine:

    @staticmethod
    def generate(metrics):

        recommendations = []

        if metrics["accuracy"] < 0.85:
            recommendations.append("Improve scoring calibration")

        if metrics["f1"] < 0.80:
            recommendations.append("Review decision thresholds")

        if not recommendations:
            recommendations.append("System performing well")

        return recommendations
