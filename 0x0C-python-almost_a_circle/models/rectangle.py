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
        """ Docstring of __init__ method
        Args:
            width (int): integer representing width of rectangle
            height (int): integer representing height of rectangle
            x (int): integer representing a coordinate
            y (int): integer representing a cooordinate
            id (int): integer representing an identification number
        """
        self.x = x
        self.y = y
        super().__init__(id)
        self.height = height
        self.width = width

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter
        Args:
            value (int): Contains whatever was inside of width """
        if (type(value) != int):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter
        Args:
            value (int): Contains whatever was inside of height """
        if (type(value) != int):
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x coordinate getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ x coordinate setter
        Args:
            value (int): Contains whatever was inside of x """
        if (type(value) != int):
            raise TypeError("x must be an integer")
        if (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y coordinate getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y coordinate setter
        Args:
            value (int): Contains whatever was inside of y """
        if (type(value) != int):
            raise TypeError("y must be an integer")
        if (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Docstring of area of the rectangle """
        return self.__width * self.__height

    def display(self):
        """ Docstring of the display of the rectangle based on
        width and height """
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
        """ Docstring __str__ string """
        return "[Rectangle] ({}) {}/{} - {}/{}\
                ".format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ Docstring update, where attributes and dictionaries are actualized
        Args:
            *args (pointer to array): Contains all arguments passed by multiple
            parameter transfer
            **kwargs (double pointer to dictionary): If *args does not exist
            then use this to create a dictionary
        """
        attributes = ["id", "width", "height", "x", "y"]
        if len(args) > 0:
            count = 0
            for arg in args:
                setattr(self, attributes[count], arg)
                count += 1
        else:
            for key, values in kwargs.items():
                setattr(self, key, values)

    def to_dictionary(self):
        """ Docstring to_dictionary method that returns the
        dictionary representation of a Rectangle """
        return self.__dict__
