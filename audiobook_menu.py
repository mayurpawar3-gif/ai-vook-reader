def show_main_menu(metadata, total_sections):

    print("\n")
    print("=" * 50)
    print("        AI AUDIOBOOK ENGINE")
    print("=" * 50)

    print(f"\nBook: {metadata['title']}")
    print(f"Author: {metadata['author']}")
    print(f"Sections Found: {total_sections}")

    print("\nChoose an option:\n")

    print("1. Generate Intro")
    print("2. Generate Next Section")
    print("3. Generate Full Audiobook")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    return choice