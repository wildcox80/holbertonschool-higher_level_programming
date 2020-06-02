#!/usr/bin/python3
"""
   0-lookup.py: returns the list of available attributes and methods
"""


def lookup(obj):
    """
        Returns the list of available attributes and methods obj
    """
    return dir(obj)
