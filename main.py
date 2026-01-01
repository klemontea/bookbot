from stats import count_words, count_chars, sort_dicts
import sys


def main():
    book_path = get_book_path()
    file_contents = get_book_text(book_path)
    num_of_words = count_words(file_contents)
    num_of_chars_mapping = count_chars(file_contents)
    num_of_chars_map_sorted = sort_dicts(num_of_chars_mapping)
    
    print_report(book_path, num_of_words, num_of_chars_map_sorted)

def get_book_text(filepath: str):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def print_report(book_path: str, total_words: int, char_num_dicts: list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")

    for item in char_num_dicts:
        if str(item['char']).isalpha():
            print(f"{item["char"]}: {item["num"]}")

    print("============= END ===============")

def get_book_path():
    args = sys.argv
    if len(args) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    return args[1]
    

main()