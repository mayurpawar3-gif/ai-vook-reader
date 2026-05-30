from narrative_state import NarrativeState

from energy_detector import EnergyDetector

from tension_detector import TensionDetector



class NarrativeEngine:

    def __init__(self):

        self.energy_detector = EnergyDetector()

        self.tension_detector = TensionDetector()

    def analyze(self, text):

        state = NarrativeState()

        state.energy = (
            self.energy_detector.detect(text)
        )

        state.tension = (
            self.tension_detector.detect(text)
        )

        return state