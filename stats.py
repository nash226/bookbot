def get_num_words(book_string):
    """A function that counts the total number of words"""

    return len(book_string.split())

def get_char_count(book_string):
    """A function that takes text from the book as a string
    and returns the number of times each character appears in 
    the string in a ditctionary."""

    char_dict = {}

    for word in book_string.split():
        for char in word.lower():
            char_dict[char] = char_dict.get(char, 0) + 1
    
    return char_dict

def descending_sort(char_dict):
    """ This function takes a dictionary of characters and returns a
    dict of characters seen in descending order"""

    sorted_dict = dict(sorted(char_dict.items(), key=lambda x: x[1], reverse=True))

    return sorted_dict



