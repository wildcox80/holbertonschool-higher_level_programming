#!/usr/bin/python3
"""
    12-student.py: class Student that defines a student
    by: (based on 11-student.py)
"""


class Student:
    """ Define class Student """

    def __init__(self, first_name, last_name, age):
        """ Define obj class Student """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            Returns a dictionary representation of a
            Student
        """
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for a in attrs:
            try:
                new_dict[a] = self.__dict__[a]
            except Exception:
                pass
        return new_dict
