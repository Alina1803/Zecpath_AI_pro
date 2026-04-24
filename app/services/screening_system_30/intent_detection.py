import os
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from app.services.screening_system_30.preprocessor import clean_text

# Constants
MODEL_PATH = "models/intent_model30.pkl"


def train_intent_model(data):
    """
    Train intent classification model and save it
    """

    # Ensure models directory exists
    os.makedirs("models", exist_ok=True)

    # Prepare data
    texts = [clean_text(d["text"]) for d in data]
    labels = [d["label"] for d in data]

    # Initialize fresh instances (avoids reuse bugs)
    vectorizer = CountVectorizer()
    model = MultinomialNB()

    # Train
    X = vectorizer.fit_transform(texts)
    model.fit(X, labels)

    # Save model
    with open(MODEL_PATH, "wb") as f:
        pickle.dump({
            "vectorizer": vectorizer,
            "model": model
        }, f)

    print("✅ intent_model.pkl saved successfully!")


def load_model():
    """
    Load model safely
    """
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            "❌ Model not found! Please run training first."
        )

    with open(MODEL_PATH, "rb") as f:
        saved = pickle.load(f)

    return saved["vectorizer"], saved["model"]


def predict_intent(text, return_confidence=False):
    """
    Predict intent from input text

    Args:
        text (str): input sentence
        return_confidence (bool): if True, returns probability

    Returns:
        intent OR (intent, confidence)
    """
    vectorizer, model = load_model()

    text = clean_text(text)
    X = vectorizer.transform([text])

    prediction = model.predict(X)[0]

    if return_confidence:
        prob = model.predict_proba(X).max()
        return prediction, round(float(prob), 3)

    return prediction