#!/usr/bin/python3
"""
    4-inherits_from.py: returns True if the object 
    is an instance of a class that inherited
"""

def inherits_from(obj, a_class):
    """
        Return True if obj is a instance of the class
        otherwise False
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
