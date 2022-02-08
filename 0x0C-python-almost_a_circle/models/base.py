#!/usr/bin/python3
""" Module class """
import json
import os


class Base():
    """ Base class defined """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Docstring of __init__ method
        Args:
            id (int): integer representing identification number """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Docstring to_json_string method which returns the JSON
        string representation of list_dictionaries.
        Args:
            list_dictionaries (list): list of dictionaries"""
        if (list_dictionaries is None or len(list_dictionaries) == 0):
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Docstring save_to_file method that writes the JSON string
        representation of list_objs to a file.
        Args:
            list_objs (list): list of instances who inherits of Base """
        empty_list = []
        with open("{}.json".format(cls.__name__), "w", encoding='utf-8') as f:
            if list_objs is None:
                f.write("[]")
            for x in list_objs:
                empty_list.append(x.to_dictionary())
            f.write(Base.to_json_string(empty_list))

    @staticmethod
    def from_json_string(json_string):
        """ Doctsring from_json_string method that returns the list of the JSON
        string representation json_string.
        Args:
            json_string (string): string representation of a list
            of dictionaries """
        empty_list = []
        if json_string is None:
            return empty_list
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Docstring create method that returns instances with all attributes
        already set.
        Args:
            **dictionary (double pointer): double pointer to a dictionary """
        if cls.__name__ == "Square":
            new_attr = cls(1)
        if cls.__name__ == "Rectangle":
            new_attr = cls(1, 1)
        new_attr.update(**dictionary)
        return new_attr

    @classmethod
    def load_from_file(cls):
        """ Docstring load_from_file mathod that returns a list
        of instances """
        filename = "{}.json".format(cls.__name__)
        empty_list = []
        catch = []
        isFile = os.path.isfile(filename)
        if isFile:
            with open(filename, "r", encoding='utf-8') as f:
                catch = cls.from_json_string(f.read())
            for inst in catch:
                empty_list.append(cls.create(**inst))
            return empty_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Docstring save_to_file_csv method that serializes and
        deserializes in CSV.
        Args:
            list_objs (list):
        """
        filename = "{}.csv".format(cls.__name__)
        empty_list = []
        with open(filename, 'w', encoding='utf-8') as f:
            if list_objs == empty_list or list_objs is None:
                f.write("[]")
            for x in list_objs:
                empty_list.append(x.to_dictionary())
            f.write(cls.to_json_string(empty_list))

    @classmethod
    def load_from_file_csv(cls):
        """ Docstring load_from_file_csv method that returns a
        list of instances """
        filename = "{}.csv".format(cls.__name__)
        empty_list = []
        catch = []
        isFile = os.path.isfile(filename)
        if isFile:
            with open(filename, "r", encoding='utf-8') as f:
                catch = cls.from_json_string(f.read())
            for inst in catch:
                empty_list.append(cls.create(**inst))
            return empty_list
