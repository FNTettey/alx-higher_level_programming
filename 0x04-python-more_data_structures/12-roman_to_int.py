#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not isinstance(roman_string, str) or
            roman_string is None):
        return (0)
 
    rn = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000}
    value = 0
    for x in range(len(roman_string)):
        if x != len(roman_string) - 1:
            if roman_string[x] == 'I':
                if roman_string[x + 1] == 'X':
                    value = value - 1
                    continue
                elif roman_string[x + 1] == 'V':
                    value = value - 1
                    continue
            elif roman_string[x] == 'X':
                if roman_string[x + 1] == 'C':
                    value = value - 10
            elif roman_string[x] == 'C':
                if roman_string[x + 1] == 'M':
                    value = value - 100
        value = value + rn[roman_string[x]]    
    return(value)
