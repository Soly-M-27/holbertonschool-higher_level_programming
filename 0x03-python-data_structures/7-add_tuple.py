#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    res = [0, 0]
    empty_tuple = ()
    if tuple_a != empty_tuple or tuple_b != empty_tuple:
        for x in range(2):
            try:
                res[x] += tuple_a[x]
            except:
                res[x] += 0
            try:
                res[x] += tuple_b[x]
            except:
                res[x] += 0
        return res
