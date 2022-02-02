#!/usr/bin/python3
""" Module function """


def write_file(filename="", text=""):
    """ write_file defined """

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
    return len(text)
