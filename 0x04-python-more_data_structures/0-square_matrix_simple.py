#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqr = lambda x: x * x
    new_matrix = []
    for row in matrix:
        C = list(map(sqr, row))
        new_matrix.append(C)
    return new_matrix

