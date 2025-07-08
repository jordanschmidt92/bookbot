import sys
from stats import count_words, count_characters, sort_character_dict

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def print_book_report(path_to_file):
    book_text = get_book_text(path_to_file)
    num_words = count_words(book_text)
    char_dict = count_characters(book_text)
    sorted_char_dict = sort_character_dict(char_dict)
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_char_dict:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print_book_report(sys.argv[1])
    print("============= END ===============")

main()