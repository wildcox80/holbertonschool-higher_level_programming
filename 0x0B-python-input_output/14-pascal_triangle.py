#!/usr/bin/python3
"""
14-main - Pascals Triangle
"""


def pascal_calculation(my_list):
    ''' calculate numbers inside list '''
    new_list = []
    prev = 0
    counter = 0

    for i in my_list:
        new_list.append(i + prev)
        prev = i
        counter += 1

    # append last element
    new_list.append(my_list[-1])

    return new_list

def pascal_triangle(n):
    if n <= 0:
        return []

    my_list = [[1]]
    for i in range(n - 1):
        new_list = pascal_calculation(my_list[-1])
        my_list.append(new_list)
    return my_list
