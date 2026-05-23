import re

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer(
    'all-MiniLM-L6-v2'
)


def split_into_paragraphs(text):

    paragraphs = re.split(r'\n\s*\n', text)

    paragraphs = [
        p.strip()
        for p in paragraphs
        if len(p.strip()) > 80
    ]

    return paragraphs


def detect_scene_changes(paragraphs):

    embeddings = model.encode(paragraphs)

    sections = []

    current_section = [paragraphs[0]]

    for i in range(1, len(paragraphs)):

        similarity = cosine_similarity(
            [embeddings[i - 1]],
            [embeddings[i]]
        )[0][0]

        # lower similarity = topic shift
        if similarity < 0.55:

            sections.append("\n\n".join(current_section))

            current_section = []

        current_section.append(paragraphs[i])

    if current_section:
        sections.append("\n\n".join(current_section))

    return sections


def detect_dialogue_density(text):

    dialogue_count = len(
        re.findall(r'".+?"', text)
    )

    total_sentences = max(
        1,
        len(text.split("."))
    )

    density = dialogue_count / total_sentences

    return density


def analyze_structure(text):

    paragraphs = split_into_paragraphs(text)

    print(f"Paragraphs Found: {len(paragraphs)}")

    sections = detect_scene_changes(paragraphs)

    analyzed_sections = []

    for i, section in enumerate(sections):

        dialogue_density = detect_dialogue_density(section)

        analyzed_sections.append({
            "title": f"Section {i+1}",
            "content": section,
            "dialogue_density": dialogue_density
        })

    return analyzed_sections