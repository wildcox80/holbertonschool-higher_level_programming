#!/usr/bin/python3
"""
    2-matrix_divide.py: divides all elements of a matrix
    row is row in matrix
    element is column in matrix
"""


def matrix_divided(matrix, div):
    """Divide elements in a matrix"""
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix is [[]] of integers/floats")

    size = -1
    for row in matrix:
        if type(row) is list:
            if size == -1:
                size = len(row)
            else:
                if size != len(row):
                    raise TypeError
                ("Each row of the matrix must have the same size")
            for element in row:
                if type(element) is not int and type(element) is not float:
                    raise TypeError
                ("matrix must be a matrix [[]] of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
    new_matrix = [[]]
    print(new_matrix)
