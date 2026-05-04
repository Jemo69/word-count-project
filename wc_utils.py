"""
this the utils file
"""

from pathlib import Path


def word_count_utils(
    file_path: Path, target_word: str, case_sensitive: bool
) -> tuple[int, str] | None:
    """
    this is the word count utils function
    it takes in a file path, a target word, and a boolean for case sensitivity
    and returns a tuple of the number of times the target word appears in the file
    """
    try:
        with open(file_path, "r") as my_file:
            content = my_file.read()

        if not case_sensitive:
            content_to_search = content.lower()
            word_to_find = target_word.lower()
        else:
            content_to_search = content
            word_to_find = target_word

        word_list = content_to_search.split()
        total = 0
        for w in word_list:
            clean_word = w.strip(".,!?;:\"'()[]{}")
            if clean_word == word_to_find:
                total = total + 1

        just_filename = file_path.name
        result_line = (
            "The word '"
            + target_word
            + "' appears "
            + str(total)
            + " time(s) in: "
            + just_filename
        )
        return total, result_line
    except Exception as error:
        print("Could not read file: " + str(file_path) + " — " + str(error))
        return None
