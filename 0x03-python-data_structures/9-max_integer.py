#!/usr/bin/python3
def max_integer(my_list=[]):
    """ returns the largest value in a list."""
    if len(my_list) == 0:
        max = None
    else:
        for i in range(len(my_list)):
            if i == 0:
                max = my_list[i]
            elif my_list[i] > max:
                max = my_list[i]
    return(max)
