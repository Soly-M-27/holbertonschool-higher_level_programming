#!/usr/bin/python3
""" Module function """


def append_write(filename="", text=""):
    """ append_write defined """

    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text)
    return len(text)
