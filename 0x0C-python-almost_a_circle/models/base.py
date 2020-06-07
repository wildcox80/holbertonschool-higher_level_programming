#!/usr/bin/python3
"""
    1-base.py: Model class Base
    Wilder Rincon : 1588@holbertonschool.com
"""


class Base:
    """
        Define Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize public instance attr id

        Args:
            id ([int], optional): [description]. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = id
            self.id = Base.__nb_objects
