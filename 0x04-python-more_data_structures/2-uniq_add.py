#!/usr/bin/python3
def uniq_add(my_list=[]):
    """ adds all unique integers in a list."""
    new = []
    sum = 0
    for i in range(len(my_list)):
        if my_list[i] not in new:
            new.append(my_list[i])
    for x in range(len(new)):
        sum = sum + new[x]
    return(sum)
