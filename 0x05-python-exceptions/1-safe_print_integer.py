#!/usr/bin/python3
def safe_print_integer(value):
    """Prints an integer.
    Args:
        value (int): The number tp be printed.
    Returns:
        The number of elements printed.
    """
    try:
        print("{:d}".format(value))
        return(True)
    except (TypeError, ValueError):
        return(False)
