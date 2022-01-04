#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    T_or_F_list = []
    for i in my_list:
        if i % 2 == 0:
            T_or_F_list.append(True)
        else:
            T_or_F_list.append(False)
    return T_or_F_list
