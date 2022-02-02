#!/usr/bin/python3
""" Module function """


def read_file(filename=""):
    """ read_file defined """
    with open(filename) as f:
        for line in f:
            print(line, end="")
