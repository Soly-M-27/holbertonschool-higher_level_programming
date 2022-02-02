#!/usr/bin/python3
""" Module function """
import json


def load_from_json_file(filename):
    """ load_from_json_file defined """

    with open(filename, "r", encoding='utf-8') as f:
        return json.load(f)
