#!/usr/bin/python3
"""
    6-to_json_string.py: returns an object (Python data structure)
    represented by a JSON string
"""


import json


def save_to_json_file(my_obj, filename):
    with open(filename, mode='w', encoding='UTF-8') as f:
        json.dump(my_obj, f)
