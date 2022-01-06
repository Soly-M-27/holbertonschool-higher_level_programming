#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for k, val in zip(key, value):
        a_dictionary[key] = value
    return a_dictionary
