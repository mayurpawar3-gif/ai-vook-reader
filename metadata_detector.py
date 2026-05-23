import re


def detect_metadata(pages):

    title = "Unknown Title"
    author = "Unknown Author"

    first_pages = pages[:5]

    combined = "\n".join(
        page["text"]
        for page in first_pages
    )

    lines = combined.split("\n")

    cleaned_lines = [
        line.strip()
        for line in lines
        if len(line.strip()) > 3
    ]

    # title = first meaningful line
    title = cleaned_lines[0]

    # smarter author detection
    for line in cleaned_lines:

        lower = line.lower()

        if lower.startswith("by "):

            author = line.replace("By ", "").replace("by ", "")
            break

    return {
        "title": title,
        "author": author
    }