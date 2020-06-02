#!/usr/bin/python3
"""
    2-is_same_class.py: Return True or False is instance exactly
"""


def is_same_class(obj, a_class):
    """
        Check if instance is same
    """
    return issubclass(a_class, type(obj))
