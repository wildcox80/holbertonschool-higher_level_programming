#!/usr/bin/python3
def number_keys(a_dictionary):
    for key, value in sorted(a_dictionary.items()):print("{} : {}".format(key, value))
