#!/usr/bin/python3
import hidden_4
str = dir(hidden_4)
string_to_compare = str[0][0]
len = len(str)
for i in range(0, len):
    if str[i][0] == string_to_compare:
        continue
    else:
        print(str[i])
