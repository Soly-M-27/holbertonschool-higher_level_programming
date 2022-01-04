#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        print(" ".join("{:d}".format(var) for var in i))
