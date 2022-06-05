#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replace an element in a copied list at a specific position."""
    copy = []
    length = len(my_list)
    if idx < 0 or idx > length - 1:
        return(my_list)
    else:
        copy = [x for x in my_list]
        copy[idx] = element
    return (copy)
