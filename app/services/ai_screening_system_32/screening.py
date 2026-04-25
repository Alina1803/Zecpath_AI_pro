def screen_candidate(data: list, model):
    prediction = model.predict([data])[0]
    probability = model.predict_proba([data])[0][1]

    return {
        "selected": bool(prediction),
        "confidence_score": round(float(probability), 2)
    }