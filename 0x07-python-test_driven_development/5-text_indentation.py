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

    string = ".?:"

    idx = 0

    while idx < len(text):
        print(text[idx], end="")
        if text[idx] in string:
            print("\n")
            while text[idx + 1] == " ":
                idx += 1
        idx += 1
