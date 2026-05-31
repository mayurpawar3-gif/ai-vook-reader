from emotion import detect_emotion


class EmotionDetector:

    def detect(self, text):

        results = detect_emotion(text)

        best = max(
            results,
            key=lambda x: x["score"]
        )

        emotion = best["label"]

        intensity = round(
            best["score"],
            2
        )

        return emotion, intensity