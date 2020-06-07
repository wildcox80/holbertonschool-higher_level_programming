#!/usr/bin/python3
"""
    2-rectangle.py: Model class Rectangle that inherits from Base
    Wilder Rincon : 1588@holbertonschool.com
"""


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):

        super().__init__(id)
        self.x = x
        self.y = y
        self.id = id