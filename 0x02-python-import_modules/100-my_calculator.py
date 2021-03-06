#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    l = len(sys.argv)
    if l != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if sys.argv[2] not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    dic = {"+": add, "-": sub, "*": mul, "/": div}
    a, op, b = int(sys.argv[1]), sys.argv[2], int(sys.argv[3])
    print("{} = {}".format(' '.join(sys.argv[1:]), dic[op](a, b)))
