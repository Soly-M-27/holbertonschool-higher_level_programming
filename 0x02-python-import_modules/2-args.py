#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv
    x = len(argv)
    if x == 1:
        print("{} arguments.".format(x-1))
    elif x == 2:
        print("{} argument:".format(x-1))
        print("{}: {}".format(x-1, argv[x-1]))
    elif x >= 1:
        print("{} arguments:".format(x-1))
        for i in range(1, x):
            print("{}: {}".format(i, argv[i]))
