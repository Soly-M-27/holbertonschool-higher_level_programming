#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    total_len = len(my_list)
    if idx < 0:
        return None
    if idx > total_len:
        print(*my_list)
    else:
        my_list[idx] = element
        return my_list
