#!/usr/bin/python3
""" Module function """
import json


def save_to_json_file(my_obj, filename):
    """ save_to_json_file defined """

    with open(filename, "w", encoding='utf-8') as f:
        f.write(json.JSONEncoder().encode(my_obj))
    return json.JSONEncoder().encode(my_obj)
