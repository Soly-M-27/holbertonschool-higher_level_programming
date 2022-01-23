#!/usr/bin/python
""" Task 3: function that prints a square with the character # """


def print_square(size):
    """
    Given a number type int. print a square of hashtags

    :param size: int
    :return: void

    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    else:
        for x in range(size):
            for x in range(size):
                print("#", end="")
            print()
