#!/usr/bin/python3
""" Task 4: function that prints a text with 2
    new lines after each of these characters: ., ? and : """


def text_indentation(text):
    """
    Given a string, create new lines after each instance of
    the following symbols:
    .
    ?
    :

    :param text: str
    :return: void
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for x in text:
        print(x, end="")
        if x == ".":
            print("\n")
        elif x == "?":
            print("\n")
        elif x == ":":
            print("\n")
