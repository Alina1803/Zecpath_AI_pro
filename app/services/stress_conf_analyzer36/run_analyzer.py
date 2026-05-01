from app.services.stress_conf_analyzer36.confidence_analyzer import calculate_confidence
from app.services.stress_conf_analyzer36.sentiment_engine import sentiment_score
from app.services.stress_conf_analyzer36.stress_detector import stress_score
from app.services.stress_conf_analyzer36.contradiction_detector import detect_contradiction

from app.config.weights36 import *

import os
import json
from datetime import datetime



def normalize(value):
    return max(0, min(value / 100, 1))



def save_output(data):
    folder_path = "data/processed"
    os.makedirs(folder_path, exist_ok=True)

    file_path = os.path.join(folder_path, "output_36.json")

    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

    return file_path


# -----------------------------
# Main Analyzer
# -----------------------------
def analyze_behavior(text, duration, save=True):
    confidence = calculate_confidence(text, duration)["confidence_score"]
    sentiment = sentiment_score(text)["sentiment_score"]
    stress = stress_score(text)
    contradiction = detect_contradiction(text)

    final_score = (
        normalize(confidence) * CONFIDENCE_WEIGHT +
        normalize(sentiment) * SENTIMENT_WEIGHT +
        normalize(stress) * STRESS_WEIGHT +
        normalize(contradiction) * CONTRADICTION_WEIGHT
    )

    result = {
        "input": {
            "text": text,
            "duration": duration
        },
        "confidence": confidence,
        "sentiment": sentiment,
        "stress": stress,
        "contradiction": contradiction,
        "behavioral_score": round(final_score * 100, 2),
        "timestamp": datetime.now().isoformat()
    }

    # Save result
    if save:
        save_output(result)

    return result