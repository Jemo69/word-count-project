from wc_utils import word_count_utils
from pathlib import Path
import sys
import os


def main() -> None:
    """
    Main function to count words in a file or directory.
    """
    if len(sys.argv) >= 4:
        path_input = sys.argv[1]
        search_word = sys.argv[2]
        case_sensitive = sys.argv[3].lower() == "yes"
    else:
        print(f"Current Directory: {os.getcwd()}")
        print(f"Files: {os.listdir(os.getcwd())}")
        path_input = input("Enter a file path or directory path to open: ")
        search_word = input("Enter the word you want to count: ")
        case_sensitive_prompt = input(
            "Should the search be case-sensitive? Enter 'yes' or 'no': "
        )
        case_sensitive = case_sensitive_prompt.lower() == "yes"

    path = Path(path_input)

    if path.is_file():
        result = word_count_utils(path, search_word, case_sensitive)
        print(f"{path.name}: {result}")

    elif path.is_dir():
        # Use .iterdir() for a more idiomatic pathlib approach
        for item in path.iterdir():
            if item.is_file():
                result = word_count_utils(item, search_word, case_sensitive)
                print(f"{item.name}: {result}")
    else:
        print("Sorry, that path doesn't seem to exist. Please try again.\n")


if __name__ == "__main__":
    main()
