#!/usr/bin/python3
""" Module class """

Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    """ Square defined """

    def __init__(self, size):
        """ Comment """
        self.__size = size
        BaseGeometry.integer_validator(self, "size", size)
        BaseGeometry.integer_validator(self, "size", size)

    def area(self):
        """ Comment """
        return self.__size * self.__size

    def __str__(self):
        """ Comment """
        return "[Square] {}/{}".format(self.__size, self.__size)
