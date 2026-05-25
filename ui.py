import os
from datetime import datetime


def clear():

    os.system("cls")


def header():

    clear()

    print("\n")
    print("======================================")
    print("           AI VOOK READER")
    print("      Narrative Intelligence v1")
    print("======================================")
    print("\n")


def show_book_info(metadata,total_sections,current_title, current_index):

    print(f"Book      : {metadata['title']}")
    print(f"Author    : {metadata['author']}")
    print(f"Chapters  : {total_sections}")
    print(f"Runtime   : Active")
    print(f"Progress  : {current_index} / {total_sections}")

    if current_title:
        print(f"Current   : {current_title}")
    print("\n")


def show_menu():

    print("--------------------------------------")
    print("1. Generate Intro")
    print("2. Generate Current Chapter")
    print("3. Generate Full Audiobook")
    print("4. Exit")
    print("--------------------------------------")