#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    C = set(set_1) ^ set(set_2)
    return C