#!/usr/bin/python3
import sys
def check_string(argv):
    try:
        int(argv)
        return True
    except ValueError:
        return False


for arg in sys.argv[1:]:
    if not check_string(arg):
        break

nums = [int(arg) for arg in sys.argv[1:]]
sum = sum(nums)

print("{}".format(sum))
