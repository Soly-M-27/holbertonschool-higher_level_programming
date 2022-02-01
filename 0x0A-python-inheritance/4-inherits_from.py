#!/usr/bin/python3
""" Module class """


def inherits_from(obj, a_class):
    """ is_kind_of_class defined """

    if issubclass(type(obj), a_class) and not type(obj) is a_class:
        return True
    else:
        return False
