#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    a = 10
    b = 5
    sum = calc.add(a, b)
    sub = calc.sub(a, b)
    product = calc.mul(a, b)
    quotient = calc.div(a, b)
    print("{} + {} = {}".format(a, b, sum))
    print("{} - {} = {}".format(a, b, sub))
    print("{} * {} = {}".format(a, b, product))
    print("{} / {} = {}".format(a, b, quotient))
