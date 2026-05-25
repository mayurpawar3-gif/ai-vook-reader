import re


def looks_like_chapter(line):

    line = line.strip()

    # empty
    if not line:
        return False

    # too short
    if len(line) < 2:
        return False

    # too long
    if len(line) > 60:
        return False

    # garbage keywords
    blocked = [
        "copyright",
        "contents",
        "index",
        "title page",
        "acknowledgements",
        "about the author",
        "more books",
    ]

    lower = line.lower()

    for word in blocked:

        if word in lower:
            return False

    # reject URLs
    if "http" in lower:
        return False

    # reject lines with too many symbols
    symbol_count = len(
        re.findall(r"[^a-zA-Z0-9\s\-]", line)
    )

    if symbol_count > 5:
        return False

    # reject paragraph-like lines
    words = line.split()

    if len(words) > 8:
        return False

    # VALID PATTERNS

    patterns = [

        # Chapter 1
        r"^chapter\s+\d+",

        # CHAPTER ONE
        r"^chapter\s+[a-z]+",

        # 1. Introduction
        r"^\d+\.",

        # Roman numerals
        r"^[IVXLC]+\.",

        # standalone title
        r"^[A-Z][a-zA-Z0-9\s\-\']+$",
    ]

    for pattern in patterns:

        if re.match(pattern, line, re.IGNORECASE):
            return True

    # fallback:
    # title-like lines
    capitalized_words = sum(
        1 for w in words
        if w[:1].isupper()
    )

    if capitalized_words >= max(1, len(words) // 2):
        return True

    return False


def extract_toc(pages):

    toc_started = False

    toc_entries = []

    toc_page_count = 0

    for page in pages[:20]:

        text = page["text"]

        lines = text.split("\n")

        # detect TOC start
        if any(
            "contents" in line.lower()
            or "table of contents" in line.lower()
            for line in lines
        ):

            toc_started = True

        if not toc_started:
            continue

        toc_page_count += 1

        for line in lines:

            cleaned = line.strip()

            if looks_like_chapter(cleaned):

                toc_entries.append(cleaned)

        # stop after few TOC pages
        if toc_page_count >= 5:
            break

    # remove duplicates
    final_entries = []

    for item in toc_entries:

        if item not in final_entries:

            final_entries.append(item)

    print("\nTOC FOUND:\n")

    for item in final_entries:

        print(item)

    return final_entries