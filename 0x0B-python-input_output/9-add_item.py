#!/usr/bin/python3
"""
    function for read and safe argv in
    Json format in file
"""
import sys
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

filename = "add_item.json"
my_list = []
try:
    my_list = load_from_json_file(filename)
except Exception:
    pass
finally:
    for i in range(1, len(sys.argv)):
        my_list.append(sys.argv[i])
    save_to_json_file(my_list, filename)
