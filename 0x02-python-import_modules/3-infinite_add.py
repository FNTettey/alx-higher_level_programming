#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum = 0
    length = len(argv)
    for i in range(length):
        if i > 0:
            sum = sum + int(argv[i])
    print(sum)
