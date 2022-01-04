#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    res = [0, 0]

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
