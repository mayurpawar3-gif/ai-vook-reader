import re


def normalize(text):

    text = text.lower()

    text = re.sub(
        r'[^a-z0-9\s]',
        '',
        text
    )

    text = re.sub(
        r'\s+',
        ' ',
        text
    )

    return text.strip()


def title_match_score(title, page_text):

    title = normalize(title)

    lines = page_text.split("\n")

    score = 0

    for i, line in enumerate(lines):

        clean_line = normalize(line)

        # exact line match
        if clean_line == title:

            score += 100

        # title appears inside line
        elif title in clean_line:

            score += 40

        # appears near top of page
        if i < 8 and title in clean_line:

            score += 30

        # short isolated line
        if (
            len(clean_line.split()) <= 6
            and title in clean_line
        ):

            score += 20

    return score


def find_best_page(title, pages):

    best_score = 0

    best_page = -1

    for i, page in enumerate(pages):

        text = page["text"]

        score = title_match_score(
            title,
            text
        )

        if score > best_score:

            best_score = score

            best_page = i

    # confidence threshold
    if best_score < 50:

        return -1

    return best_page


def map_chapters(toc, pages):

    matches = []

    chapters = []

    print("\nMAPPING CHAPTERS...\n")

    for title in toc:

        page_index = find_best_page(
            title,
            pages
        )

        if page_index != -1:

            matches.append(
                (title, page_index)
            )

            print(
                f"[FOUND] {title} -> page {page_index + 1}"
            )

        else:

            print(
                f"[MISS]  {title}"
            )

    # sort by page order
    matches.sort(
        key=lambda x: x[1]
    )

    # remove backward duplicates
    cleaned = []

    used_pages = set()

    for title, page in matches:

        if page not in used_pages:

            cleaned.append(
                (title, page)
            )

            used_pages.add(page)

    # build chapter slices
    for i in range(len(cleaned)):

        title, start_page = cleaned[i]

        if i + 1 < len(cleaned):

            end_page = cleaned[i + 1][1]

        else:

            end_page = len(pages)

        content = []

        for page in pages[start_page:end_page]:

            content.append(
                page["text"]
            )

        chapter_text = "\n\n".join(content)

        chapters.append(
            (
                title,
                chapter_text
            )
        )

    return chapters