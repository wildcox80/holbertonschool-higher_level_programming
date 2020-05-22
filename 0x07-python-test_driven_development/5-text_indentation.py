#!/usr/bin/python3
"""
    5-text_indentation.py: prints a text with 2 new lines
    after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints text with 2 lines after each `.`, `?`, and `:`
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    start = True
    space_count = 0
    for c in text:
        if c == " " and start:
            continue
        if c == " ":
            space_count += 1
            continue
        else:
            print("{}".format(" " * space_count), end="")
            space_count = 0
        if c == "." or c == "?" or c == ":":
            print("{}\n".format(c))
            start = True
        else:
            start = False
            print("{}".format(c), end="")
