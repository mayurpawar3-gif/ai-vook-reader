import asyncio

from pdf_reader import extract_text
from narrator import generate_voice
from emotion import detect_emotion

from metadata_detector import detect_metadata
from story_detector import find_story_start

from title_generator import generate_section_title
from book_parser import parse_book
from audiobook_menu import show_main_menu
from progress_tracker import (save_progress,load_progress)

PDF_PATH = "books/book.pdf"


async def generate_intro(metadata, total_sections):

    intro = f"""
    Welcome to your AI audiobook experience.

    Today's book is:

    {metadata['title']}

    Written by:

    {metadata['author']}

    This book contains {total_sections} sections.

    Starting your journey now.
    """

    await generate_voice(
        intro,
        "neutral",
        "output/intro.mp3"
    )

    print("Intro generated.")


async def generate_section(title, content, index):

    print(f"\nGenerating {title}")

    generated_title = generate_section_title(
        content[:1500]
    )

    print(f"AI Section Title: {generated_title}")

    emotions = detect_emotion(content[:1000])

    top_emotion = max(
        emotions,
        key=lambda x: x["score"]
    )

    emotion_label = top_emotion["label"]

    print(f"Emotion: {emotion_label}")

    output_file = f"output/chapter_{index}.mp3"

    narration = f"""

    Now reading:

    {generated_title}

    {content[:5000]}
    """

    await generate_voice(
        narration,
        emotion_label,
        output_file
    )

    print(f"Generated: {output_file}")


async def main():

    print("Reading PDF...")

    pages = extract_text(PDF_PATH)

    print(f"Pages Extracted: {len(pages)}")

    metadata = detect_metadata(pages)

    print(f"Book Title: {metadata['title']}")
    print(f"Author: {metadata['author']}")

    story_start = find_story_start(pages)

    print(f"Story starts near page: {story_start + 1}")

    story_pages = pages[story_start:]

    text = "\n\n".join(
        page["text"]
        for page in story_pages
    )

    print("Parsing book structure...")

    sections = parse_book(text)

    print(f"Found {len(sections)} sections.")

    await generate_intro(
        metadata,
        len(sections)
    )

    current_index = load_progress()
    print(f"\nResuming from section {current_index + 1}" ) 

    while True:

        choice = show_main_menu(
            metadata,
            len(sections)
        )

        if choice == "1":

            await generate_intro(
                metadata,
                len(sections)
            )

        elif choice == "2":

            if current_index >= len(sections):

                print("\nAll sections generated.")
                continue

            title, content = sections[current_index]

            await generate_section(
                title,
                content,
                current_index + 1
            )

            current_index += 1
            save_progress(current_index)

        elif choice == "3":

            while current_index < len(sections):

                title, content = sections[current_index]

                await generate_section(
                    title,
                    content,
                    current_index + 1
                )

                current_index += 1
                save_progress(current_index)

            print("\nFull audiobook generated.")

        elif choice == "4":

            print("\nExiting AI Audiobook Engine.")
            break

        else:

            print("\nInvalid choice.")
        
    print("Session completed.")


if __name__ == "__main__":

    asyncio.run(main())