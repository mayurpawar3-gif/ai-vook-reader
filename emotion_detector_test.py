from emotion_detector import EmotionDetector

detector = EmotionDetector()

emotion, intensity = detector.detect(
    """
    He was terrified.

    The darkness surrounded him.

    His hands shook.
    """
)

print(emotion)
print(intensity)