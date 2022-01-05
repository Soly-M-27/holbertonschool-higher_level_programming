#!/usr/bin/python3
def max_integer(my_list=[]):
    top = my_list[0]
    for x in my_list:
        if x > top:
            top = x
    return top
