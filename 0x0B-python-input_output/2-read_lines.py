#!/usr/bin/python3
""" 2-read_lines.py: Write a function that reads n lines
    of a text file (UTF8) and prints it to stdout
"""


def read_lines(filename="", nb_lines=0):
    """ Function numbers of lines file """

    counter = 0
    with open(filename, mode='r', encoding="UTF8") as file:
        if nb_lines <= 0:
            print(file.read(), end="")
            return
        counter = 0
        for counter, line in enumerate(file):
            if counter == nb_lines:
                break
            print(line, end="")
