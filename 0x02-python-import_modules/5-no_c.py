#!/usr/bin/python3
def no_c(my_string):
    s = "".join(x for x in my_string if x != 'c' if x != 'C')
    return s
