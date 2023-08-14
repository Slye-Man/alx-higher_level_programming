#!/usr/bin/python3
"""A function that prints integers in reverse"""

def print_reversed_list_integer(my_list=[]):
    if my_list:
        for i in reversed(my_list):
            print("{:d}".format(i))
