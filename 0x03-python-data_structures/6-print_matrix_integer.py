#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        first = True
        for i in row:
            if not first:
                print(" ", end="")
            first = False
            print("{:d}".format(i), end="")
        print("")
