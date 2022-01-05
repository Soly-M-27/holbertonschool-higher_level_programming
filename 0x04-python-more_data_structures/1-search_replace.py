#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for x in my_list:
        new_list.append(x)

    for y in range(0, len(new_list)):
        if new_list[y] == search:
            new_list[y] = replace
    return new_list
