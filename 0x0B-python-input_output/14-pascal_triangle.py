#!/usr/bin/python3
"""
14-main - Pascals Triangle
"""


def pascal_triangle(n):
    """
        Define function pascal triangle
    """

    matrix = []
    for i in range(n):
        matrix.append([])
    for i in range(n):
        if i == 0:
            matrix[0].append(1)
            continue
        if i == 1:
            matrix[1].append(1)
            matrix[1].append(1)
            continue
        for j in range(i + 1):
            if j == 0 or j == i:
                matrix[i].append(matrix[i-1][j-1])
            else:
                res = matrix[i-1][j] + matrix[i-1][j-1]
                matrix[i].append(res)
    return(matrix)
