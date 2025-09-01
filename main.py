import sys
from stats import get_num_words, get_char_count, descending_sort

def get_book_text(filepath):
    """This function converts our to a string and returns it"""

    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    book = sys.argv[1]
    text = get_book_text(book)
    num_words = get_num_words(text)
    char_dict = get_char_count(text)
    ordered_dict = descending_sort(char_dict)

    print(f'============ BOOKBOT ============')
    print(f'Analyzing book found at {book}')              #TODO
    print(f'----------- Word Count ----------')
    print(f'Found {num_words} total words')
    print(f'--------- Character Count -------')
    for char in ordered_dict:
        print(f'{char}: {ordered_dict[char]}')
    print(f'============= END ===============')        


if __name__ == '__main__':
    main()