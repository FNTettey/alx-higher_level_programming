#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    from sys import argv
    length = len(argv)
    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        op = argv[2]
        b = int(argv[3])
    sum = calc.add(a, b)
    sub = calc.sub(a, b)
    product = calc.mul(a, b)
    quotient = calc.div(a, b)
    if op == '-':
        print("{} - {} = {}".format(a, b, sub))
    elif op == '+':
        print("{} + {} = {}".format(a, b, sum))
    elif op == '/':
        print("{} / {} = {}".format(a, b, quotient))
    elif op == "*":
        print("{} * {} = {}".format(a, b, product))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
