#!/usr/bin/python3
""" Module function """
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"
open(filename, "a", encoding='utf-8')
my_list = []

try:
    my_list = load_from_json_file(filename)
    my_list.extend(sys.argv[1:])
except ValueError:
    my_list = []
save_to_json_file(my_list, filename)
