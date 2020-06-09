#!/usr/bin/python3
"""
    square.py: Model class Square that inherits from Rectangle
    Wilder Rincon : 1588@holbertonschool.com
"""
from models.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        """ Initiliaze method square

        Args:
            size ([int]): [size square]
            x (int, optional): [x value]. Defaults to 0.
            y (int, optional): [y value]. Defaults to 0.
            id ([int], optional): [id value]. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns string representation of a square"""
        return "[Square] ({}) {:d}/{:d} - {:d}"\
            .format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ getter method for width """
        return self.width
        
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value       
        