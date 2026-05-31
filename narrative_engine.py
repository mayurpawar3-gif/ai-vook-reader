from narrative_state import NarrativeState

from energy_detector import EnergyDetector

from tension_detector import TensionDetector
from emotion_detector import EmotionDetector



class NarrativeEngine:

    def __init__(self):

        self.energy_detector = EnergyDetector()
        self.emotion_detector = EmotionDetector()
        self.tension_detector = TensionDetector()

    def analyze(self, text):

        state = NarrativeState()

        state.energy = (
            self.energy_detector.detect(text)
        )

        state.tension = (
            self.tension_detector.detect(text)
        )
        
        emotion, intensity = (
            self.emotion_detector.detect(text)
        )

        state.emotion = emotion

        state.emotion_intensity = intensity
        return state