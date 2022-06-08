#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """returns a set of elements present in only one set."""
    new = {}
    new = set_1 ^ set_2
    return(new)
