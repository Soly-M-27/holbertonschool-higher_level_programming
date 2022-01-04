#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    total_len = my_list.copy()
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        total_len[idx] = element
        return (total_len)
