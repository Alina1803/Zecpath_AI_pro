class IntentClassifier:

    def classify(self, text):
        text = text.lower()

        if any(k in text for k in ["gst", "tax", "audit", "tds"]):
            return "technical"

        elif any(k in text for k in ["experience", "worked", "handled"]):
            return "experience"

        elif any(k in text for k in ["salary", "ctc", "lpa"]):
            return "salary"

        elif any(k in text for k in ["join", "available", "notice"]):
            return "availability"

        return "general"