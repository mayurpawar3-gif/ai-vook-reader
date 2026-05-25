import difflib


def normalize(text):

    return (
        text.lower()
        .replace("\n", " ")
        .strip()
    )


def find_best_match(title, lines):

    best_score = 0
    best_index = -1

    normalized_title = normalize(title)

    for i, line in enumerate(lines):

        candidate = normalize(line)

        score = difflib.SequenceMatcher(
            None,
            normalized_title,
            candidate
        ).ratio()

        if score > best_score:

            best_score = score
            best_index = i

    return best_index, best_score


def map_chapter(
    toc_entries,
    text
):

    lines = text.split("\n")

    matches = []

    # find headings
    for title in toc_entries:

        index, score = find_best_match(
            title,
            lines
        )

        if score > 0.6:

            matches.append(
                (title, index)
            )

    matches.sort(
        key=lambda x: x[1]
    )

    chapters = []

    for i in range(len(matches)):

        title, start_idx = matches[i]

        if i < len(matches) - 1:

            end_idx = matches[i + 1][1]

        else:

            end_idx = len(lines)

        content = "\n".join(
            lines[start_idx:end_idx]
        )

        chapters.append(
            (title, content)
        )

    return chapters