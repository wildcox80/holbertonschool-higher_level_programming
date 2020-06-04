#!/usr/bin/python3
""" 
    8-load_from_json_file.py: creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """load Json form file
    Args:
        filename ([str]): name of file Json
    Returns:
        [python-obj]:
    """

    with open(filename, mode='r', encoding="utf-8") as f:
        return json.loads(f.read())
