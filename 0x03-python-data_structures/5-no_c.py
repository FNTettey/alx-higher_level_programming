#!/usr/bin/python3
def no_c(my_string):
    """Removes all the Cs from a string."""
    new = ""
    for i in range(len(my_string)):
        if my_string[i] != 'c' and  my_string[i] != 'C':
            new = new + my_string[i]
    return(new)
