#!/usr/bin/python3
""" Task 2: Function that prints 'My name is <first name> <last name>' """


def say_my_name(first_name, last_name=""):
    """
    Given the names from main, print the first and last name
    of the user

    :param first_name: str
    :param last_name: str
    :return: void

    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is", first_name, last_name)
