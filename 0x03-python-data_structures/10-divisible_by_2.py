#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """ returns whether a value in a list is divisable by 2."""
    new = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
                new.append(True)
            else:
                new.append(False)
    return(new)
