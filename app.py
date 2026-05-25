import asyncio

from pdf_reader import extract_text
from narrator import generate_voice
from emotion import detect_emotion
from file_utils import clean_filename
from metadata_detector import detect_metadata
from story_detector import find_story_start
from chapter_mapper import map_chapters
from toc_detector import extract_toc
from narrative_label import generate_narrative_label
from text_cleaner import clean_text
from ui import ( header, show_book_info, show_menu )
from content_cleaner import clean_content
from subtitle_formatter import format_narration

PDF_PATH = "books/book.pdf"


async def generate_intro(metadata, total_sections):

    intro = f"""
    Welcome to your AI audiobook experience.

    Today's book is:

    {metadata['title']}

    Written by:

    {metadata['author']}

    This book contains {total_sections} chapters.

    Starting your journey now.
    """

    await generate_voice(
        intro,
        "neutral",
        "output/intro.mp3"
    )

    print("\nIntro generated.")


async def generate_section(title, content, index):

    print(f"\nGenerating Chapter: {title}")

    narrative_label = generate_narrative_label(
        content[:3000]
    )

    print(
        f"Narrative Tone   : "
        f"{narrative_label}"
    )
    
    emotions = detect_emotion(
        content[:1000]
    )

    top_emotion = max(
        emotions,
        key=lambda x: x["score"]
    )

    emotion_label = top_emotion["label"].capitalize()

    print(f"Emotion Detected: {emotion_label}")

    safe_title = clean_filename(title)

    output_file = (
        f"output/"
        f"{index:02d}_{safe_title}.mp3"
    )
    content = clean_content(content)
    content = clean_text(content)

    content = format_narration(content)      

    # add pause after opening speaker label
    words = content.split()

    if len(words) > 3:

        first_word = words[0]

        if first_word.istitle():

            words[0] = first_word + "..."

            content = " ".join(words)
    
    narration = f"""

    Chapter Title...

    {title}...

    {content[:5000]}

    """

    await generate_voice(
        narration,
        emotion_label,
        output_file
    )

    print(
        f"\nChapter Generated:"
        f"\n{output_file}"
    )


async def main():

    print("Reading PDF...")

    pages = extract_text(PDF_PATH)

    print(
        f"Pages Extracted: "
        f"{len(pages)}"
    )

    metadata = detect_metadata(pages)

    print(
        f"Book Title: "
        f"{metadata['title']}"
    )

    print(
        f"Author: "
        f"{metadata['author']}"
    )

    story_start = find_story_start(pages)

    print(
        f"Story starts near page: "
        f"{story_start + 1}"
    )

    story_pages = pages[story_start:]


    print("\nExtracting TOC...")

    toc = extract_toc(pages)

    print(
        f"TOC Chapters Found: "
        f"{len(toc)}"
    )

    print("\nMapping chapters...")

    sections = map_chapters(
        toc,
        story_pages
    )

    print(
        f"TOC Chapters Loaded: "
        f"{len(toc)}"
    )

    current_index = 0

    while True:

        header()

        current_title = None

        if current_index < len(sections):

            current_title = (
                sections[current_index][0]
            )

        show_book_info(metadata, len(toc), current_title, current_index)
        show_menu()

        choice = input(
            "\nEnter your choice: "
        )

        # INTRO
        if choice == "1":

            await generate_intro(
                metadata,
                len(sections)
            )

            input(
                "\nPress Enter to continue..."
            )

        # CURRENT CHAPTER
        elif choice == "2":

            if current_index >= len(sections):

                print(
                    "\nAll chapters generated."
                )

                input(
                    "\nPress Enter to continue..."
                )

                continue

            title, content = sections[current_index]

            await generate_section(
                title,
                content,
                current_index + 1
            )

            current_index += 1

            input(
                "\nPress Enter to continue..."
            )

        # FULL AUDIOBOOK
        elif choice == "3":

            while current_index < len(sections):

                title, content = (
                    sections[current_index]
                )

                await generate_section(
                    title,
                    content,
                    current_index + 1
                )

                current_index += 1

            print(
                "\nFull audiobook generated."
            )

            input(
                "\nPress Enter to continue..."
            )

        # EXIT
        elif choice == "4":

            print(
                "\nExiting AI Vook Reader."
            )

            break

        else:

            print("\nInvalid choice.")

            input(
                "\nPress Enter to continue..."
            )

    print("\nSession completed.")


if __name__ == "__main__":

    asyncio.run(main())