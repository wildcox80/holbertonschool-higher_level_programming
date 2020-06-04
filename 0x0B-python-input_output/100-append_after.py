#!/usr/bin/python3
""" 100-append_after.py: inserts a line of text to a file,
    after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """ inserts new_string after each line contains search_string """

    text_holder = ""
    with open(filename) as file:
        line = file.readline()
        while line:
            text_holder += line
            if search_string in line:
                text_holder += new_string
            line = file.readline()
    with open(filename, 'w') as f:
        f.write(text_holder)
