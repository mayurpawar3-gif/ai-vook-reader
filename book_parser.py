import re


def clean_text(text):

    text = text.replace('\r', '\n')

    text = re.sub(r'[ \t]+', ' ', text)

    text = re.sub(r'(?<!\n)\n(?!\n)', ' ', text)

    text = re.sub(r'\n{2,}', '\n\n', text)

    return text.strip()


def semantic_fallback_split(
    text,
    chunk_size=12000
):

    chunks = []

    for i in range(0, len(text), chunk_size):

        chunk = text[i:i + chunk_size]

        title = f"Section {len(chunks)+1}"

        chunks.append(
            (title, chunk)
        )

    return chunks


def parse_book(text):

    text = clean_text(text)

    print("Using semantic fallback splitting...")

    return semantic_fallback_split(text)
    