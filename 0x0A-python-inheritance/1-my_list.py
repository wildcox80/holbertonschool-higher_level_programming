#!/usr/bin/python3
"""
    1-my_list.py: Write a class MyList that inherits from list
"""


class MyList(list):
    """ Class MyList inherits from list"""

    def print_sorted(self):
        """
            Print list my_list
        """
        print(sorted(self))
