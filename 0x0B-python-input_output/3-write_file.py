#!/usr/bin/python3
"""
    3-write_file.py: returns the number of characters written
"""


def write_file(filename="", text=""):
    """ Function numbers of lines file """

    with open(filename, mode='w', encoding="UTF-8") as f:
        return f.write(text)
