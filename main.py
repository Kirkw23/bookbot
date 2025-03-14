from stats import count_words
from stats import count_characters
from stats import create_2_keys
import sys

def get_book_text(book_path):
    with open(book_path) as f:
        book = f.read()
    return book


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        book_text = get_book_text(book_path)
        count = count_words(book_text)
        output = count_characters(book_text)
        fin = create_2_keys(output)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {count} total words")
        print("--------- Character Count --------")
        for i in fin:
            if i['character'].isalpha():
                print(f"{i['character']}: {i['count']}")
        print("============ BOOKBOT ============")
main()


