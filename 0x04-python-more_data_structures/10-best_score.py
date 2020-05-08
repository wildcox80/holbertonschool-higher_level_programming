#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return
    best = []
    for new in a_dictionary:
        best.append(new)
    return max(best)
