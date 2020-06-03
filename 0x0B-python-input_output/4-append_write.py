#!/usr/bin/python3
"""
    4-append_file.py: returns the number of characters added
"""


def append_write(filename="", text=""):
    """ Function append character in str """

    with open(filename, mode='a', encoding="UTF-8") as f:
        return f.write(text)


