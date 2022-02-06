#!/usr/bin/python3
""" Module class Rectangle """

from models.base import Base



class Rectangle(Base):
    """ Class Rectangle Defined """
    __width = None
    __height = None
    __x = None
    __y = None

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if (type(value) != int):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if (type(value) != int):
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if (type(value) != int):
            raise TypeError("x must be an integer")
        if (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if (type(value) != int):
            raise TypeError("y must be an integer")
        if (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        string = ""
        if self.__width == 0 or self.__height == 0:
            print("")
        for x in range(self.__height):
            if self.__y != 0 and x == 0:
                for cor_y in range(self.__y):
                    string += '\n'
            if self.__x != 0:
                for cor_x in range(self.__x):
                    string += " "
            string += '#'
            for y in range(self.__width - 1):
                x *= y
                string += '#'
            string += '\n'
        print(string[:-1])

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args):
        attributes = ["id", "width", "height", "x", "y"]
        count = 0
        for arg in args:
            setattr(self, attributes[count], arg)
            count += 1
