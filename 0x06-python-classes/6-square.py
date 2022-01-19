#!/usr/bin/python3
""" Module with the class Square """


class Square:
    """ Square Defined """
    __size = None
    __position = None

    def __init__(self, size=0, position=(0, 0)):
        """ Docstring of __init___ method

        Args:
            size (int): size from main to be displayed
            position (tuple): tuple of 2 positive integers
        """
        self.size = size
        """ int: Docstring *after* attribute, with type specified """
        self.position = position
        """ tuple: Docstring *after* attribute, with type tuple specified """

    @property
    def size(self):
        """ Docstring of size """
        return self.__size
        """ returns the size attribute with value """

    @size.setter
    def size(self, value):
        """ Docstring of size

        Args:
            value (int): Contains size from __size attribute
        """
        if (type(value) != int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value
        """ set size """

    @property
    def position(self):
        """ Docstring of position getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """ Docstring of position setter

        Args:
            value (tuple): Contains tuple from __position attribute
        """
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
        """ Assigning tuple in attribute """

    def area(self):
        """ Docstring of area """
        return self.__size * self.__size
        """ size squared """

    def my_print(self):
        """ Docstring of my_print printer """
        if (self.__size == 0):
            print()
        else:
            for x in range(self.__position[1]):
                print("" * self.__position[1])
            for y in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
