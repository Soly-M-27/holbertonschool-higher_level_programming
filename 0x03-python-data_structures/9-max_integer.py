#!/usr/bin/python3
def max_integer(my_list=[]):
    top = 0
    length = len(my_list)
    for x in range(length):
        if my_list[x] > my_list[x + 1]:
            top = my_list[x]
        else:
            top = my_list[x + 1]
        return top
