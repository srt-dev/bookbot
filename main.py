from stats import get_word_count
from stats import get_char_count
from stats import get_sorted_dictionaries
import sys

def get_padded_string(input: str, pad_char: str, pad_length: int) -> str:
    to_return = f" {input} "
    input_length = len(to_return)
    if input_length >= pad_length:
        return to_return
    else:
        while len(to_return) < pad_length:
            to_return = f"{pad_char}{to_return}{pad_char}"
    return to_return[:pad_length]

def get_header(header: str = "", char_length: int = 33) -> str:
    return get_padded_string(input=header, pad_char="=", pad_length=char_length)

def get_sub_header(header: str = "", char_length: int = 33) -> str:
    return get_padded_string(input=header, pad_char="-", pad_length=char_length)

def get_book_text(filepath: str) -> str:
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents


def main():
    # Handle args
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    print(get_header("BOOKBOT"))
    print(f"Analyzing book found at {book_path}...")
    book_text = get_book_text(filepath=book_path)

    print(get_sub_header("Word Count"))
    word_count = get_word_count(book_text)
    print(f"Found {word_count} total words")

    print(get_sub_header("Character Count"))
    char_counts = get_char_count(book_text)
    sorted_char_counts = get_sorted_dictionaries(char_counts)
    for char_count in sorted_char_counts:
        if char_count['char'].isalpha():
            print(f"{char_count['char']}: {char_count['num']}")
    # print(book_text)

    print(get_header("END"))


main()



# ============ BOOKBOT ============
# Analyzing book found at books/frankenstein.txt...
# ----------- Word Count ----------
# # Found 75767 total words
# --------- Character Count -------

# Analyzing book found at books/frankenstein.txt...
# ---------- Word Count ----------
# -------- Character Count --------

# e: 44538
# t: 29493
# a: 25894
# o: 24494
# i: 23927
# n: 23643
# s: 20360
# r: 20079
# h: 19176
# d: 16318
# l: 12306
# m: 10206
# u: 10111
# c: 9011
# f: 8451
# y: 7756
# w: 7450
# p: 5952
# g: 5795
# b: 4868
# v: 3737
# k: 1661
# x: 691
# j: 497
# q: 325
# z: 235
# æ: 28
# â: 8
# ê: 7
# ë: 2
# ô: 1
# ============= END ===============
# ============ BOOKBOT ============