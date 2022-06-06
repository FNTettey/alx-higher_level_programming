#!/usr/bin/python3
def multiple_returns(sentence):
    """ returns a tuple with the length of a string and its first character."""
    new = ()
    if len(sentence) == 0:
        first = None
    else:
        first = sentence[0]
    new = (len(sentence), first)
    return (new)
