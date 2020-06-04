#!/usr/bin/python3
"""
14-main - Pascals Triangle
"""


def pascal_triangle(n):
    if n <= 0:
        return []

    my_list = [[1]]
    for counter in range(1, n):
        row = [1]
        for i in range(1, counter):
            row.append(my_list[counter - 1][i - 1] + my_list[counter - 1][i])
        row.append(1)
        my_list.append(row)
    return my_list
