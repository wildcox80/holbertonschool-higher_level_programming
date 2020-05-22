#!/usr/bin/python3
"""
    3-say_my_name.py: print first_name + last_name
    first_name is str
    last_name is str
"""


def say_my_name(first_name, last_name=""):
    """Print Full Name first_name + last_name

    Arguments:
        first_name {[str]} -- [print first name]
        last_name {[str]} -- [print last name]

    Raises:
        TypeError: [first_name must be a string]
        TypeError: [last_name must be a string]
    """
    if first_name:
        if type(first_name) is not str:
            raise TypeError("first_name must be a string")
        if type(last_name) is not str:
            raise TypeError("last_name must be a string")
        print("My name is {} {}".format(first_name, last_name))
