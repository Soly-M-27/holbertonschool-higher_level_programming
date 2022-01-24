#!/usr/bin/python3
""" Module with the class Square """


class Rectangle:
    """ Rectangle Defined """

    def __init__(self, width=0, height=0):
        """ Docstring of __init__ method

        Args:
            width (int): width from main
            height (int): height from  main
        """
        self.__height = height
        """ int: Docstring *after* attribute, with type specified """
        self.__width = width
        """ int: Docstring *after* attribute, with type specified """

        @property
        def width(self):
            """ Docstring of width getter """
            return self.__width

        @width.setter
        def width(self, value):
            """ Docstring of width setter

            Args:
                value (int): Contains int from __width attribute
            """
            if type(value) != int:
                raise TypeError("width must be an integer")
            if self.__width < 0:
                raise ValueError("width must be >= 0")
            self.__width = value
            """ Assigning int to attribute """

        @property
        def height(self):
            """ Docstring of heigth getter """
            return self.__height

        @height.setter
        def height(self, value):
            """ Docstring of heigth setter

            Args:
                value (int): Contains int from __heigth attribute
            """
            if type(value) != int:
                raise TypeError("height must be an integer")
            if self.__heigth < 0:
                raise ValueError("height must be >= 0")
            self.__heigth = value
            """ Assigning int to attribute """
