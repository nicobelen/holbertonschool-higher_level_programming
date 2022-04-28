#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    def no_of_argu(*args):
        return(len(args))


ar = len(sys.argv) - 1
if ar == 0:
    print("0 arguments.")
elif ar == 1:
    print("1 argument:")
    for i in range(1, len(sys.argv)):
        print(i, ": ", sys.argv[i], sep="")
else:
    print(ar, "arguments:")
    for i in range(1, len(sys.argv)):
        print(i, ": ", sys.argv[i], sep="")
