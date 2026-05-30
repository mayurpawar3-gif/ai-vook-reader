import re

from vocabulary.energy_words import (
    ACTION_WORDS,
    CALM_WORDS
)


class EnergyDetector:

    def detect(self, text):

        words = re.findall(
            r"\w+",
            text.lower()
        )

        score = 0

        for word in words:

            if word in ACTION_WORDS:
                score += 2

            elif word in CALM_WORDS:
                score -= 1

        score = max(0, min(score, 10))

        return round(score / 10, 2)