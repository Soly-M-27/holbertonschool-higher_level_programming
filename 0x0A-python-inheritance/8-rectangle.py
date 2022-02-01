#!/usr/bin/python3
""" Module with Rectangle class inheriting BaseGeometry """


class BaseGeometry:
    """ BaseGeometry defined """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ Rectangle defined """
    __width = None
    __height = None

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, width, height)
