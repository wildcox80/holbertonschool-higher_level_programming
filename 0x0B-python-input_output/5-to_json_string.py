#!/usr/bin/python3
"""
    5-to_json_string.py: returns the JSON representation of an object (string)
"""


import json


def to_json_string(my_obj):
    """ Function convert JSON an object(string) """

    return json.dumps(my_obj)
