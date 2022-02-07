#!/usr/bin/python3
""" Module class Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square inhereting Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.height)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
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
        return (self.__dict__)
