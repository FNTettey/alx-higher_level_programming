#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """sorts a dictionary by ordered keys."""
    [print(f"{k}: {a_dictionary[k]}") for k in sorted(a_dictionary)]
