from emotion import detect_emotion


class EmotionDetector:

    def detect(self, text):

        results = detect_emotion(text)

        print("\nEmotion Candidates:")

        for r in results[:5]:

            print(
                r["label"],
                round(r["score"], 3)
            )

        top_emotions = sorted(
            results,
            key=lambda x: x["score"],
            reverse=True
        )

        primary = top_emotions[0]

        secondary = [

            (
                item["label"],
                round(item["score"], 3)
            )

            for item in top_emotions[1:3]
        ]

        return (
            primary["label"],
            round(primary["score"], 2),
            secondary
        )