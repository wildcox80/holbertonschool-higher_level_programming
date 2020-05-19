#!/usr/bin/python3
"""1-square.py: class Square that defines a square
private instantiation attribute of size"""


class Square:
    """Creates Square type"""

    def __init__(self, size=0):
        """Initializes Square with size"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
