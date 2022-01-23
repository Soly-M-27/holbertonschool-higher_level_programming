#!/usr/bin/python3
""" Task 0: Function to add integers """


def add_integer(a, b=98):

    """
    Given two integers, return the sum.

    :param a: int
    :param b=98: int
    :return: int

    """

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")

    return a + b
