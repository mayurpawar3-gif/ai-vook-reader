import re


def clean_line(line):

    line = line.strip()

    line = re.sub(
        r'\s+',
        ' ',
        line
    )

    return line


def looks_like_title(line):

    if len(line) < 3:
        return False

    if len(line) > 60:
        return False

    words = line.split()

    if len(words) > 8:
        return False

    return True


def extract_year(text):

    years = re.findall(
        r'(19\d{2}|20\d{2})',
        text
    )

    if years:

        return years[0]

    return "Unknown"


def detect_metadata(pages):

    title = "Unknown Title"

    author = "Unknown Author"

    year = "Unknown"

    # scan first pages
    first_text = "\n".join(
        page["text"]
        for page in pages[:10]
    )

    lines = first_text.split("\n")

    cleaned_lines = []

    for line in lines:

        line = clean_line(line)

        if line:

            cleaned_lines.append(line)

    # TITLE DETECTION
    for line in cleaned_lines:

        if looks_like_title(line):

            # ignore bad metadata words
            blocked = [
                "copyright",
                "contents",
                "acknowledgements",
                "all rights reserved",
            ]

            if any(
                b in line.lower()
                for b in blocked
            ):
                continue

            title = line.title()

            break

    # AUTHOR DETECTION
    for i, line in enumerate(cleaned_lines):

        lower = line.lower()

        # Written by
        if "written by" in lower:

            possible = line.replace(
                "Written by",
                ""
            ).strip()

            if possible:

                author = possible.title()

        # by Rahul Jain
        elif lower.startswith("by "):

            possible = line[3:].strip()

            if len(possible.split()) <= 4:

                author = possible.title()

        # next line heuristic
        elif (
            title.lower() in lower
            and i + 1 < len(cleaned_lines)
        ):

            next_line = cleaned_lines[i + 1]

            if len(next_line.split()) <= 4:

                author = next_line.title()

    # YEAR
    year = extract_year(first_text)

    return {
        "title": title,
        "author": author,
        "year": year
    }