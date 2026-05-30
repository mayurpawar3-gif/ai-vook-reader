from dataclasses import dataclass


@dataclass
class NarrativeState:

    scene_type: str = "unknown"
    emotion: str = "neutral"
    emotion_intensity: float = 0.0
    energy: float = 0.0
    tension: str = "stable"
    narrative_role: str = "unknown"

    def summary(self):

        return f"""    
Narrative Analysis
------------------
Scene Type      : {self.scene_type}
Emotion         : {self.emotion}
Intensity       : {self.emotion_intensity}
Energy          : {self.energy}
Tension         : {self.tension}
Role            : {self.narrative_role}
"""