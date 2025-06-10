import sys
from stats import get_num_words, get_chars_dict, sorted_list


def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_list = sorted_list(chars_dict)
    print_report(book_path, num_words,chars_list)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(book_path, num_words, chars_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for chars in chars_list:
        if chars["char"].isalpha() == True:
            print(f"{chars["char"]}: {chars["num"]}")
        else:
            pass
    print("============= END ===============")

main()
