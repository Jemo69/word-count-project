from wc_utils import word_count_utils
from pathlib import Path
import sys
import os


def main():
    """
    this is the main function
    """
    if len(sys.argv) > 1:
        path = sys.argv[1]
        search_word = sys.argv[2]
        case_sensitive_prompt = sys.argv[3]
    else:
        print(f"{os.getcwd()}")
        print(f"Files:{os.listdir(os.getcwd())}")
        path = Path(input("Enter a file path or directory path to open: "))
        search_word = input("Enter the word you want to count: ")
        case_sensitive_prompt = input(
            "Should the search be case-sensitive? Enter 'yes' or 'no': "
        )

        if case_sensitive_prompt.lower() == "yes":
            case_sensitive = True
        elif case_sensitive_prompt.lower() == "no":
            case_sensitive = False
    # this if one file or list of files in a directory

    if isinstance(path, str):
        path = Path(path)
    if path.is_file():
        print(word_count_utils(path, search_word, case_sensitive))
    # this if a directory
    elif path.is_dir():
        directory_contents = os.listdir(path)
        for item in directory_contents:
            full_item_path = Path(f"{path} + {os.sep} + {item}")
            if os.path.isfile(full_item_path):
                print(word_count_utils(full_item_path, search_word, case_sensitive))
    else:
        print("Sorry, that path doesn't seem to exist. Please try again.\n")


if __name__ == "__main__":
    main()
