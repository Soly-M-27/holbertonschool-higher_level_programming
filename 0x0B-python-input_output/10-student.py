#!/usr/bin/python3
""" Module of class """


class Student:
    """ class Student """
    first_name = None
    last_name = None
    age = None

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Comment """
        if attrs is None:
            return self.__dict__
        dictionary = {}
        for x in attrs:
            try:
                dictionary[x] = self.__dict__[x]
            except:
                pass
        return dictionary
