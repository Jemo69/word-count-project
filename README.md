# Word Count Project

Simple Python CLI for counting how many times a word appears in a file or in every file inside a directory.

## Requirements

- Python 3.12+
- Optional: `uv` if you prefer running the script with `uv run`

## Usage

Run from the project root:

```bash
python main.py <path> <word> <yes|no>
```

Example:

```bash
python main.py notes.txt hello no
```

Or with `uv`:

```bash
uv run main.py notes.txt hello yes
```

## Behavior

- If `<path>` is a file, the script counts matches in that file.
- If `<path>` is a directory, the script counts matches in each file directly inside that directory.
- Matching punctuation such as `.,!?;:"'()[]{} ` is stripped before comparison.
- Use `yes` for case-sensitive matching and `no` for case-insensitive matching.

## Interactive Mode

If you do not pass the command-line arguments, the script prompts for:

- a file or directory path
- the word to count
- whether the search should be case-sensitive

## Tests

The repository includes a small test script in `test.py`.

```bash
python test.py
```

## Project Files

- `main.py` - CLI entrypoint
- `wc_utils.py` - word counting logic
- `test.py` - simple script-based test
