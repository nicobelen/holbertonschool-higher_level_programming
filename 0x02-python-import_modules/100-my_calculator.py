#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    args = len(sys.argv) - 1
    
    if args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    
    a = sys.argv[1]
    b = sys.argv[3]

    if sys.argv[2] == '+':
        print(a, "+", b, "=", add(int(a), int(b)))
    elif sys.argv[2] == '-':
        print(a, "-", b, "=", sub(int(a), int(b)))
    elif sys.argv[2] == '*':
        print(a, "*", b, "=", mul(int(a), int(b)))
    elif sys.argv[2] == '/':
        print(a, "/", b, "=", div(int(a), int(b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
