#!/usr/bin/python3
""" Module with Rectangle class inheriting BaseGeometry """

Rectangle = __import__('8-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle defined """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "height", height)
        BaseGeometry.integer_validator(self, "width", width)

    def area(self):
        """ Comment """
        return self.__width * self.__height

    def __str__(self):
        """ Comment """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
