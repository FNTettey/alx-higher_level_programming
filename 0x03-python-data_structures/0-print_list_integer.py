#!/usr/bin/python3#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """Print all integers in a list."""
    length = len(my_list)
    for i in range(len(my_list)):
        print("{}".format(my_list[i]))
