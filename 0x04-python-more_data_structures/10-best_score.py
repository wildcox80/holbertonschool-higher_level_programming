#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return
    new_dict = []
    for new in a_dictionary:
        new_dict.append(new)
    return max(new_dict)
