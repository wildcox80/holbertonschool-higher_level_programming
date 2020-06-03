#!/usr/bin/python3
"""
    6-to_json_string.py: returns an object (Python data structure)
    represented by a JSON string
"""


import json


def from_json_string(my_str):
    """ Function return an object represented JSON(string) """

    return json.loads(my_str)
