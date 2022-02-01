#!/usr/bin/python3
""" Module with the class MyList """

class MyList(list):

    def __init__(self):
        self.list = list

    def print_sorted(self):
        """ print_sorted defined """
        new_list = []
        new_list.append(self.list)
        print(new_list)
