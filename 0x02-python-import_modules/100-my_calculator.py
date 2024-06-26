#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, mul, sub, div
    from sys import argv
    if (len(argv) - 1) < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = argv[1]
        b = argv[3]
        a = int(a)
        b = int(b)
        if argv[2] == '+':
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif argv[2] == '-':
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif argv[2] == '*':
            print("{} * {} = {}".format(a, b, mul(a, b)))
        elif argv[2] == '/':
            print("{} / {} = {}".format(a, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)