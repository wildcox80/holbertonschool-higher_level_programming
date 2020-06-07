#!/usr/bin/python3
"""
    2-rectangle.py: Model class Rectangle that inherits from Base
    Wilder Rincon : 1588@holbertonschool.com
"""
from models.base import Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initiliaze method rectangle

        Args:
            width ([int]): [width rectangle]
            height ([int]): [height rectangle]
            x (int, optional): [x value]. Defaults to 0.
            y (int, optional): [y value]. Defaults to 0.
            id ([int], optional): [id value]. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ getter method for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter method width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Getter method for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter method for height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """ getter method for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter method for x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ method getter for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter method for y """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Return area of the rectangle"""

        return self.width * self.height

    def display(self):
        """Print stdout of the rectangle"""
        a = 0
        print('\n' * self.y, end="")
        for a in range(self.height):
            print(' ' * self.x, end="")
            print('#' * self.width)
        

    def __str__(self):
        """Method that returns string representation of rectangle"""
        h, i, j = self.id, self.width, self.height
        k, l = self.x, self.y
        return("[Rectangle] ({}) {}/{} - {}/{}".format(h, k, l, i, j))

    def update(self, *args, **kwargs):
        """ Method for update attributes """
        if args and len(args) != 0:
            attrs = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                if i >= len(attrs):
                    return
                setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
 