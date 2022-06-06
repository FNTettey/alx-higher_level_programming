#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Adding two tuples together"""
    new = ()
    if len(tuple_a) >= 2:
        a1, a2 = tuple_a
    elif len(tuple_a) == 1:
        a1 = tuple_a[0]
        a2 = 0
    else:
        a1 = 0
        a2 = 0

    if len(tuple_b) >= 2:
        b1, b2 = tuple_b
    elif len(tuple_b) == 1:
        b1 = tuple_b[0]
        b2 = 0
    else:
        b1 = 0
        b2 = 0
    num1 = a1 + b1
    num2 = a2 + b2
    new = (num1, num2)
    return(new)
