#!/usr/bin/python3
""" Module with Rectangle class inheriting BaseGeometry """


class BaseGeometry:
    """ BaseGeometry defined """

    def area(self):
        return self.name * self.value

    def __str__(self):
        print("[Rectangle] {}/{}".format(self.name, self.value))

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

class Square(Rectangle):
    """ Square defined """
    __size = None

    def __init__(self, size):
        self.__size = size
        Rectangle.BaseGeometry.integer_validator(self, size, size)
