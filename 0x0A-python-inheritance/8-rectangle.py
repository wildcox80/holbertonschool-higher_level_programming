#!/usr/bin/python3
"""
    8-rectangle: Write a class Rectangle that
    inherits from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        class Rectangle inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """ private instantiation of attributes """

        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height
