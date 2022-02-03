#!/usr/bin/python3
""" Module function """
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


filename = "add_item.json"
my_list = []

try:
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    my_list = []
for args in argv[1:]:
    my_list.append(args)
save_to_json_file(my_list, filename)
