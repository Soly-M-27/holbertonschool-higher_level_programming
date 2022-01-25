#!/usr/bin/python3
""" class Rectangle module"""


class Rectangle:
    """ Define a rectangle """

    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 and self.__height == 0:
            P = 0
        else:
            P = (2 * (self.__height + self.__width))
        return P

    def __str__(self):
        string = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        for x in range(self.__height):
            string += '#'
            for y in range(self.__width - 1):
                x *= y
                string += '#'
            string += '\n'
        return string[:-1]

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)
