#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replaces an element in a list."""
    length = len(my_list)
    if idx < 0 or idx > length -1:
        return(my_list)
    else:
        my_list[idx] = element 
        return(my_list)
