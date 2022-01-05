#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        C = list(map(lambda x: x * x, row))
        new_matrix.append(C)
    return new_matrix
