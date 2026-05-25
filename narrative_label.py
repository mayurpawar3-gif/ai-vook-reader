import re


def generate_narrative_label(text):

    text = text.lower()

    patterns = {

        "Fearful Pursuit": [
            "ran",
            "behind me",
            "chased",
            "dark",
            "scream",
            "fear"
        ],

        "Psychological Tension": [
            "silence",
            "waiting",
            "stared",
            "watching",
            "cold"
        ],

        "Emotional Conflict": [
            "cry",
            "tears",
            "hurt",
            "pain",
            "alone"
        ],

        "Mystery Discovery": [
            "found",
            "letter",
            "door",
            "clue",
            "missing"
        ],

        "Violent Confrontation": [
            "blood",
            "knife",
            "attack",
            "fight",
            "dead"
        ],

        "Romantic Reflection": [
            "love",
            "kiss",
            "heart",
            "together",
            "smile"
        ],

        "Narrative Transition": [
            "morning",
            "later",
            "after",
            "suddenly",
            "next day"
        ]
    }

    scores = {}

    for label, keywords in patterns.items():

        score = 0

        for word in keywords:

            matches = len(
                re.findall(
                    re.escape(word),
                    text
                )
            )

            score += matches

        scores[label] = score

    best_label = max(
        scores,
        key=scores.get
    )

    # fallback
    if scores[best_label] == 0:

        return "Narrative Progression"

    return best_label