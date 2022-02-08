#!/usr/bin/python3
""" Module class Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square inhereting Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Docstring of the __init__ method. """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter
        Args:
            value (int): Contains whatever width of height
            number was passed """
        if (type(value) != int):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Docstring update method that assigns attributes.
        Args:
            *args (list): list of arguments passed through multiple
            parameters.
            **kwargs (double pointer): if *args does not exist,
            double pointer to dictionary will save the arguments
            in key/value form. """
        attributes = ["id", "size", "x", "y"]
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
        dictionary representation of a Square """
        return {
                "id": self.id,
                "x": self.x,
                "size": self.width,
                "y": self.y
                }

    def __str__(self):
        """ Docstring of __str__ method that returns a string """
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))
