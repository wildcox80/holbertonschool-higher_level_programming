#!/usr/bin/python3
"""
    7-save_to_json_file.py: writes an Object to a text file,
    using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """ Function return an object a text file """
    with open(filename, mode='w', encoding='UTF-8') as f:
        f.write(json.dumps(my_obj))
