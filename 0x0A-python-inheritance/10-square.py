#!/usr/bin/python3
"""
    10-square.py: Write a class Rectangle that
    inherits from BaseGeometry
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class Square inherits from 9/rectangle """

    def __init__(self, size):
        """Instantiate private instance field size"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
