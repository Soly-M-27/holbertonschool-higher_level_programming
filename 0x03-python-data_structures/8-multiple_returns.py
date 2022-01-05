#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_space = [0, ""]

    tuple_space[0] = len(sentence)
    if tuple_space[0] == 0:
        tuple_space[1] = None
    else:
        tuple_space[1] = sentence[0:1]
    return tuple(tuple_space)
