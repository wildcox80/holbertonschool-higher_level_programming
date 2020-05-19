#!/usr/bin/python3
"""5-square.py: Prints to stdout the square with the character #"""


class Square:
    """Creates  Square type"""

    def __init__(self, size=0):
        """Initializes Square with size"""

        self.size = size

    @property
    def size(self):
        """Defines square size and returns his value"""

        return self.__size

    @size.setter
    def size(self, value):
        """Defines value of size of square and checks if >= 0"""

        self.__size = value
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """Defines area of a square"""

        return self.__size * self.__size

    def my_print(self):
        """Prints stdout the square with character #"""

        for a in range(self.__size):
            for b in range(self.__size):
                print('#', end="")
            print()
        if self.__size == 0:
            print()
