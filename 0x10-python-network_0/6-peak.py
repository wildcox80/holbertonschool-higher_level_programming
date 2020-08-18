#!/usr/bin/python3
def find_peak(list_of_integers):
    """ Python function to find peak number"""

    lenght = len(list_of_integers)
    if lenght == 0:
        return
    mid = lenght//2
    high = list_of_integers[mid]
    low = list_of_integers[mid - 1]

    if (mid == lenght - 1 or high >= list_of_integers[mid + 1]) and\
            (mid == 0 or high >= low):
        return high
    elif mid != lenght - 1 and list_of_integers[mid + 1] >= high:
        return (find_peak(list_of_integers[mid:]))
    return (find_peak(list_of_integers[:mid]))
