#!/usr/bin/python3
"""
    3-say_.py: functions add two integers
    size is the size length of the square
    last_name is str
"""


def print_square(size):
    """Print square with char #

    Arguments:
        size {[lenght]} -- [size is the size length of the square]

    Raises:
        TypeError: [size must be an integer]
        TypeError: [size must be >= 0]
        TypeError: [size must be an integer]
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and type(size) < 0:
        raise TypeError("size must be an integer")
    else:
        print("{}\n".format("#" * size) * size, end="")
