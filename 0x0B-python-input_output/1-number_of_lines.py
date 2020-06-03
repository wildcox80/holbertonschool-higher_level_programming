#!/usr/bin/python3
""" 1-number_of_lines.py: Write a function that returns
    the number of lines of a text file
"""


def number_of_lines(filename=""):
    """ Function numbers of lines file """

    counter = 0
    with open(filename) as file:
        for line in file:
            counter += 1
    return counter
