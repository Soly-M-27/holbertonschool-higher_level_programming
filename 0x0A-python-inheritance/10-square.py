#!/usr/bin/python3
""" Module with Rectangle class inheriting BaseGeometry """

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Comment """
    def __init__(self, size):
        self.__size = size
        BaseGeometry.integer_validator(self, "size", size)
        BaseGeometry.integer_validator(self, "size", size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
