#!/usr/bin/python3
""" Module with the class Square """


class Square:
    """ Square Defined """
    __size = None

    def __init__(self, size=0):
        """ Docstring of __init___ method

        Args:
            size (int): size from main to be displayed
        """
        if (type(size) != int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
        """ int: Docstring *after* attribute, with type specified """

    def area(self):
        """ Area of Square squared """
        return self.__size * self.__size
        """ Return size squared """
