#!/usr/bin/python3
def element_at(my_list, idx):
    length = len(my_list)
    return (my_list[idx] if 0 <= idx < length else None)
