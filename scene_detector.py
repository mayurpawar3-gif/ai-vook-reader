import re
from typing import List

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


SCENE_TRANSITIONS = [
    "later",
    "meanwhile",
    "the next day",
    "hours later",
    "that night",
    "suddenly",
    "in the morning",
    "three years later",
]


def split_into_paragraphs(text: str):

    paragraphs = [
        p.strip()
        for p in text.split("\n\n")
        if p.strip()
    ]

    return paragraphs


def has_transition_cue(text: str):

    lower = text.lower()

    return any(
        cue in lower
        for cue in SCENE_TRANSITIONS
    )


def detect_scenes(text: str) -> List[str]:

    paragraphs = split_into_paragraphs(text)

    if len(paragraphs) <= 1:
        return [text]

    scenes = []

    current_scene = [paragraphs[0]]

    previous_embedding = model.encode(
        paragraphs[0]
    )

    for paragraph in paragraphs[1:]:

        current_embedding = model.encode(
            paragraph
        )

        similarity = cosine_similarity(
            [previous_embedding],
            [current_embedding]
        )[0][0]

        transition_detected = (
            similarity < 0.55
            or has_transition_cue(paragraph)
        )

        if transition_detected:

            scenes.append(
                "\n\n".join(current_scene)
            )

            current_scene = [paragraph]

        else:

            current_scene.append(paragraph)

        previous_embedding = current_embedding

    if current_scene:

        scenes.append(
            "\n\n".join(current_scene)
        )

    return scenes