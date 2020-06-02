#!/usr/bin/python3
"""
    7-base_geometry: Write a class BaseGeometry
    (based on 6-base_geometry.py)
"""


class BaseGeometry():
    """
        Inheritance class BaseGeometry for use def area
    """

    def __init__(self):
        pass

    """
        Define area function with raise message
    """

    def area(self):
        raise Exception("area() is no implemented")

    def integer_validator(self, name, value):
        """
            Check value input type correct
        """

        if type(value) is not int:
            raise TypeError("{} must be a integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greather than 0".format(name))
