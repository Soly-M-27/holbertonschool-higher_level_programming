#!/usr/bin/python3
""" Task 1: Function that divides all elements of a matrix """


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a number type int or float

    :param matrix: list of lists
    :param div: int or float
    :return: new_matrix

    """
    new_matrix=[]
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    length = len(matrix[0])

    for x in matrix:
        if type(x) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(x) != length:
            raise TypeError("Each row of the matrix must have the same size")
        for y in x:
            if type(y) is not int and type(y) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for arr in matrix:
        new_list=[]
        for elem in arr:
            new_list.append(round(elem / div, 2))
        new_matrix.append(new_list)
    return new_matrix
