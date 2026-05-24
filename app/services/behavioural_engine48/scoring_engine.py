from app.services.behavioural_engine48.signal_mapping import (
    calculate_behavior_score
)

from app.services.behavioural_engine48.insight_generator import (
    generate_behavior_insights
)

from app.services.behavioural_engine48.risk_detection import (
    detect_behavior_risk
)


def behavioral_pipeline(data):

    signals = {
        "eye_focus": data.eye_focus,
        "head_stability": data.head_stability,
        "engagement": data.engagement,
        "distraction": data.distraction
    }

    score = calculate_behavior_score(signals)

    insights = generate_behavior_insights(score)

    risk = detect_behavior_risk(score)

    return {
        "behavior_score": score,
        "signals": signals,
        "risk": risk,
        "insights": insights
    }