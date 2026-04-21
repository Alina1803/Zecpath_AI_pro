class ResponseAnalyzer:

    def is_off_topic(self, text):
        keywords = ["gst", "tax", "audit", "account"]
        return not any(k in text.lower() for k in keywords)

    def is_vague(self, text):
        return len(text.split()) < 5