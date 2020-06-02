#!/usr/bin/python3
"""
    2-is_same_class.py: Return True or False is instance exactly
"""


def is_same_class(obj, a_class):
    """
        Conditions correct for print exactly instance
    """
    return issubclass(a_class, type(obj))
