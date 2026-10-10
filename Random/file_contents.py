"""Question:

How can you read the words from words.txt and use a list comprehension to
collect only the words that start with A or a?

Complete the TODOs below, then display the matching words.
    TODO: Read the contents of file_path.
    TODO: Use a list comprehension to select words that start with A or a.
    TODO: Display the selected words.
"""

from pathlib import Path


def main():
    file_path = Path(__file__).with_name("words.txt")

    with open(file_path, "r", encoding="utf-8") as f:
        file_content = f.read().split()

    # word.lower().startswith("a")
    selected_words = [word for word in file_content if word.startswith("A") or word.startswith("a")]
    print(selected_words)


if __name__ == "__main__":
    main()
