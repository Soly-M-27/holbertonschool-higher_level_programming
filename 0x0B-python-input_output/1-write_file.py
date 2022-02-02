#!/usr/bin/python3
""" Module function """


def write_file(filename="", text=""):
    """ write_file defined """

    text_file = open(filename)
    if text_file:
        with open(filename, "w") as f:
            return f.write(text)
    else:
        with open(filename, "w+") as f:
            return f.wrire(text)
