from dataclasses import dataclass, field


@dataclass
class NarrativeState:

    scene_type: str = "unknown"

    primary_emotion: str = "neutral"

    emotion_intensity: float = 0.0

    secondary_emotions: list = field(
        default_factory=list
    )

    energy: float = 0.0

    tension: str = "stable"

    narrative_role: str = "unknown"

    def summary(self):

        return f"""
Narrative Analysis
------------------
Scene Type      : {self.scene_type}
Primary Emotion : {self.primary_emotion}
Intensity       : {self.emotion_intensity}
Secondary       : {self.secondary_emotions}
Energy          : {self.energy}
Tension         : {self.tension}
Role            : {self.narrative_role}
"""