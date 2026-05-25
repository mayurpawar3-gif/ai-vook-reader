import re


def clean_text(text):

    # convert line breaks into spaces
    text = text.replace("\n", " ")

    # fix broken single-letter spacing
    text = re.sub(
        r"\b([A-Za-z])\s+([a-z]{2,})",
        r"\1\2",
        text
    )

    # normalize spaces
    text = re.sub(
        r"\s+",
        " ",
        text
    )

    # clean punctuation spacing
    text = re.sub(
        r"\s+([.,!?])",
        r"\1",
        text
    )

    return text.strip()