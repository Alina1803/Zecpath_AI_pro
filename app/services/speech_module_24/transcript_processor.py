class TranscriptProcessor:

    def remove_silence_segments(self, segments, threshold=0.5):
        return [seg for seg in segments if seg['end'] - seg['start'] > threshold]

    def merge_segments(self, segments):
        text = " ".join([seg["text"] for seg in segments])
        return text

    def handle_partial_answers(self, text):
        # Simple heuristic
        if len(text.split()) < 3:
            return "[INCOMPLETE ANSWER]"
        return text

    def process(self, stt_output):
        segments = stt_output["segments"]
        
        segments = self.remove_silence_segments(segments)
        text = self.merge_segments(segments)
        text = self.handle_partial_answers(text)

        return text