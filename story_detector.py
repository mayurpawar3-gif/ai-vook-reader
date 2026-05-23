import re


def find_story_start(pages):

    patterns = [
        r'chapter\s+1',
        r'prologue',
        r'part\s+1'
    ]

    for i, page in enumerate(pages):

        text = page["text"].lower()

        for pattern in patterns:

            if re.search(pattern, text):

                return i

    # fallback
    return 5
    