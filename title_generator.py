import re


def generate_section_title(text):

    lines = text.split(".")

    for line in lines:

        cleaned = line.strip()

        if len(cleaned) > 20:

            cleaned = re.sub(
                r'\s+',
                ' ',
                cleaned
            )

            return cleaned[:60]

    return "Untitled Section"
    