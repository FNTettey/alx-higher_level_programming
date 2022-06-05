#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Print all integers in a list in reverse."""
    my_list.reverse()
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
