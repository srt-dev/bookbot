from typing import TypedDict

class CharResult(TypedDict):
    char: str
    num: int

# result: CharResult = {'char': "a", 'num': 1}

def sort_on(items):
    return items["num"]


def get_word_count(input_string: str):
    words = input_string.split()
    word_count = len(words)
    return word_count
    
def get_char_count(input_string: str) -> dict[str, int]:
    to_process: str = input_string.lower()
    to_return: dict[str, int] = {}
    for char in to_process:
        to_return[char] = 1 + to_return.get(char, 0)

    return to_return


def get_sorted_dictionaries(input: dict[str, int]) -> list[CharResult]:
    to_return = []
    for char_entry in input:
        entry: CharResult = {"char": char_entry, "num": input[char_entry]}
        to_return.append(entry)
    to_return.sort(reverse=True, key=sort_on)
    return to_return
