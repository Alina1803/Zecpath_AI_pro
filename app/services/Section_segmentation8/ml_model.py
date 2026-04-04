from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import json
import joblib   


class SectionClassifier:

    def __init__(self):
        # Initialize vectorizer and model
        self.vectorizer = TfidfVectorizer()
        self.model = LogisticRegression(max_iter=1000)

    def train(self, data_path):
        # Load labeled data
        with open(data_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        texts = [item["text"] for item in data]
        labels = [item["label"] for item in data]

        # Convert text to features
        X = self.vectorizer.fit_transform(texts)

        # Train model
        self.model.fit(X, labels)

    def predict(self, texts):
        """
        Predict labels for input text(s)

        Supports:
        - single string
        - list of strings
        """

        # 🔥 handle single string input
        if isinstance(texts, str):
            texts = [texts]

        # Transform input using trained vectorizer
        X = self.vectorizer.transform(texts)

        # Return predictions
        return self.model.predict(X)

    # 🔥 OPTIONAL (VERY USEFUL)
    def save(self, path="models/section_model.pkl"):
        import os
        os.makedirs(os.path.dirname(path), exist_ok=True)
        joblib.dump((self.vectorizer, self.model), path)

    def load(self, path="models/section_model.pkl"):
        self.vectorizer, self.model = joblib.load(path)