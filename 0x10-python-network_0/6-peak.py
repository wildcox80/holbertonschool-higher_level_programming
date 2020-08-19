#!/usr/bin/python3
"""Peak exercise"""


def find_peak(list_of_integers):
    """Finds peak in unsorted list of integers"""

    if not list_of_integers:
        return None

    length = len(list_of_integers)
    half = int(length / 2)
    if length > 1:
        if half >= half - 1 and half >= half + 1:
            return half
        if (half == length - 1 or list_of_integers[half] >=
            list_of_integers[half + 1])\
                and (half == 0 or list_of_integers[half] >=
                     list_of_integers[half - 1]):
            return list_of_integers[half]
        if list_of_integers[0] >= list_of_integers[1]:
            return list_of_integers[0]
        if list_of_integers[-1] >= list_of_integers[-2]:
            return list_of_integers[-1]
    return find_peak(list_of_integers[half:])
