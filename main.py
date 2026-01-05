from stats import get_num_words
from stats import get_num_characters
from stats import dict_to_list
import sys

def get_book_text(path_to_file):            # reads file contents
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book_path = sys.argv[1]
    text = get_book_text(book_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")

    num_words = get_num_words(text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")

    num_letters = get_num_characters(text)
    sorted_chars = dict_to_list(num_letters)

    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")

    print("============= END ===============")
main()