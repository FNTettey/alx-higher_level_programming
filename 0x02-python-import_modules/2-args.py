#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = len(argv)
    if n == 1:
        print("0 arguments.")
    elif n == 2:
        print("1 argument:")
    else:
        print(f"{n - 1} arguments:")
    for x in range(n):
        if x > 0:
            print(f"{x}: {argv[x]}")
