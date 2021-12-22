#!/usr/bin/python3
def uppercase(str):
    result = ''
    for c in str:
        if ord(c) >= 65:
            result += chr(ord(c) - 32)
    return result
