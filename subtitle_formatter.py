import re


def format_narration(text):

    lines = text.split()

    formatted = []

    for word in lines:

        clean = word.strip()

        # detect ALL CAPS short speaker labels
        if (
            clean.isupper()
            and len(clean) <= 12
        ):

            formatted.append(
                f"{clean}... "
            )

        else:

            formatted.append(
                clean + " "
            )

    return "".join(formatted)