#!/usr/bin/python3
"""
    11-student.py: Create class student
"""


class Student:
    """
        Define class Student
    """
    def __init__(self, first_name, last_name, age):
        """
            Define obj class Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
            Return dict class Student
        """
        return self.__dict__
