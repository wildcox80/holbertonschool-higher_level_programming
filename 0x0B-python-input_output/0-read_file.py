#!/usr/bin/python3
""" 0-read_file.py: Write a function that reads a text file (UTF8) """


def read_file(filename=""):
    """ Function print text encoding UTF-8 """
    with open(filename, encoding="UTF8") as file:
        for line in file:
            print(line, end="")
