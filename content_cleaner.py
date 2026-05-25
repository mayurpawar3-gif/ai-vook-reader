import re


def clean_content(text):

    # normalize line endings
    text = text.replace("\r", "\n")

    # remove page numbers
    text = re.sub(
        r'\n\s*\d+\s*\n',
        '\n',
        text
    )

    # remove repeated whitespace
    text = re.sub(
        r'[ \t]+',
        ' ',
        text
    )

    # remove multiple empty lines
    text = re.sub(
        r'\n{3,}',
        '\n\n',
        text
    )

    # remove common footer/header junk
    junk_patterns = [

        r'copyright',
        r'all rights reserved',
        r'www\.',
        r'http[s]?://',
        r'printed in',
        r'published by',

    ]

    for pattern in junk_patterns:

        text = re.sub(
            pattern,
            '',
            text,
            flags=re.IGNORECASE
        )

    # remove isolated page markers
    text = re.sub(
        r'page\s+\d+',
        '',
        text,
        flags=re.IGNORECASE
    )

    # remove duplicate consecutive lines
    lines = text.split("\n")

    cleaned_lines = []

    previous = ""

    for line in lines:

        line = line.strip()

        if not line:
            continue

        if line.lower() == previous.lower():
            continue

        cleaned_lines.append(line)

        previous = line

    text = "\n".join(cleaned_lines)

    return text.strip()