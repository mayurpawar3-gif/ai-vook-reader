import re

from vocabulary.tension_words import (
    RISING_TENSION_WORDS,
    PEAK_TENSION_WORDS,
    RELEASE_WORDS
)


class TensionDetector:

    def detect(self, text):

        words = re.findall(
            r"\w+",
            text.lower()
        )

        peak = sum(
            word in PEAK_TENSION_WORDS
            for word in words
        )

        rising = sum(
            word in RISING_TENSION_WORDS
            for word in words
        )

        release = sum(
            word in RELEASE_WORDS
            for word in words
        )

        if peak:
            return "peak"

        if rising:
            return "rising"

        if release:
            return "release"

        return "stable"