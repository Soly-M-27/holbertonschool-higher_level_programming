#!/usr/bin/python3
""" Module class """
import json


class Base():
    """ Base class defined """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        empty_list = []
        with open("{}.json".format(cls.__name__), "w", encoding='utf-8') as f:
            if list_objs is None:
                f.write("[]")
            for x in list_objs:
                empty_list.append(x.to_dictionary())
            f.write(cls.to_json_string(empty_list))

    @staticmethod
    def from_json_string(json_string):
        empty_list = []
        if json_string is None:
            return empty_list
        return json.loads(json_string)
