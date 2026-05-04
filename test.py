from pathlib import Path
from subprocess import run


def test():
    path = Path("/home/jemo/projects/prompt")
    search_word = "uv"
    case_sensitive = "yes"
    try:
        test_run = run(["uv", "run", "main.py", path, search_word, case_sensitive])
        print(test_run.stdout)
    except Exception as error:
        print(f"{error} - test failed")
    else:
        print("test passed")


if __name__ == "__main__":
    test()
